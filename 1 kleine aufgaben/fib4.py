# fib4.py
# Aus "Algorithmen in Python", Kapitel 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # Dieselbe Definition wie fib2()
    if n < 2:  # Abbruchbedingung
        return n
    return fib4(n - 2) + fib4(n - 1)  # Rekursionsbedingung


if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))