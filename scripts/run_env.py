# ----------------------------------------------------------------------------
# Copyright (c) 2021-2025 DexForce Technology Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

"""Thin launcher that defers to EmbodiChain's unified ``embodichain`` CLI.

This task package is auto-discovered by the unified CLI through the
``embodichain.tasks`` entry point declared in ``pyproject.toml``. You can
therefore launch any registered task with either of::

    embodichain run-env --gym_config configs/demo/dummy.json
    python -m embodichain run-env --gym_config configs/demo/dummy.json

This script is kept as a convenience entry point that simply calls the unified
CLI, so existing ``python scripts/run_env.py ...`` invocations keep working
while benefiting from task discovery and init-hook execution.
"""

from embodichain.lab.scripts.run_env import cli

if __name__ == "__main__":
    cli()
