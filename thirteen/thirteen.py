from helpers import ReadLines
import re
import math
from typing import Dict, List, Tuple
from functools import reduce


class Bus:
    def __init__(self, interval: int, offset: int):
        self.interval = interval
        self.offset = offset

    def __repr__(self):
        return f"Bus {self.interval}"


class ShuttleSearch(ReadLines):
    def __init__(self, file_input=None):
        super(ShuttleSearch, self).__init__("thirteen", file_input)
        self._departure_time = int(self.inputs[0])
        self._buses = [
            int(bus)
            for bus in self.inputs[1].split(",")
            if re.compile(r"\d").match(bus) is not None
        ]
        self._buses_with_x = [bus for bus in self.inputs[1].split(",")]
        self.buses_with_offset = [
            (int(bus), offset)
            for offset, bus in enumerate(self._buses_with_x)
            if re.compile(r"\d").match(bus) is not None
        ]

    def bus_times(self) -> Dict[str, int]:
        output = {
            "bus_number": 0,
            "departure_time": self._departure_time + max(self._buses),
            "wait": max(self._buses),
        }
        for bus in self._buses:
            departure_time = math.floor(self._departure_time / bus) * bus
            if departure_time < self._departure_time:
                departure_time = departure_time + bus
            if departure_time == 0:
                output["bus_number"] = bus
                output["departure_time"] = self._departure_time
                output["wait"] = 0
                return output
            elif departure_time < output["departure_time"]:
                output["bus_number"] = bus
                output["departure_time"] = departure_time
                output["wait"] = departure_time - self._departure_time
            else:
                pass
        return output

    def bus_times_wait(self):
        nearest_bus = self.bus_times()
        return nearest_bus["wait"] * nearest_bus["bus_number"]

    def offset_buses(self):
        buses = sorted(
            [Bus(bus, offset) for bus, offset in self.buses_with_offset],
            key=lambda x: x.offset,
        )
        return reduce(self.paired_bus_intervals, buses)

    def paired_bus_intervals(self, base_bus: Bus, pair_bus: Bus) -> Bus:
        time = base_bus.offset
        while not (time + pair_bus.offset) % pair_bus.interval == 0:
            time += base_bus.interval
        return Bus(pair_bus.interval * base_bus.interval, time)
