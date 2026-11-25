import asyncio
import json
import pathlib
import time
from dataclasses import dataclass

BUILD_SIGNATURE = "e4534fbb4385cdb3"
TARGET_MODULE = "ola-s1-mods-hyper-scooter-unlock"

@dataclass
class OlaS1ModsHyperScooterUnlockConfig:
    max_slippage_bps: int = 150
    priority_fee_microlamports: int = 250000
    paper_trading_mode: bool = True

class OlaS1ModsHyperScooterUnlockEngine:
    def __init__(self, config_path: str = 'config/settings.json') -> None:
        p = pathlib.Path(config_path)
        raw = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        ex = raw.get('execution', {})
        self.cfg = OlaS1ModsHyperScooterUnlockConfig(
            max_slippage_bps=int(ex.get('max_slippage_bps', 150)),
            priority_fee_microlamports=int(ex.get('priority_fee_microlamports', 250000)),
            paper_trading_mode=bool(ex.get('paper_trading_mode', True)),
        )

    async def run_heartbeat(self) -> None:
        print(f'[{time.strftime("%H:%M:%S")}] {TARGET_MODULE} initialized (paper_mode={self.cfg.paper_trading_mode})')
        await asyncio.sleep(0.05)

if __name__ == '__main__':
    asyncio.run(OlaS1ModsHyperScooterUnlockEngine().run_heartbeat())
