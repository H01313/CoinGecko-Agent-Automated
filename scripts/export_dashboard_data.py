import json
from pathlib import Path
from datetime import datetime, timezone

base = Path(__file__).resolve().parents[1]
data_dir = base / "data"
data_dir.mkdir(exist_ok=True)
now = datetime.now(timezone.utc).isoformat()

(data_dir / "latest_snapshot.json").write_text(json.dumps({
    "generated_at": now, "symbol": "XRPUSD", "price": 0.6421, "rsi": 54.28,
    "signal": "HOLD", "balance": 1000.0, "success_ratio": 0.0,
    "position": "NONE", "entry_price": None
}, indent=2), encoding="utf-8")
(data_dir / "market_data.json").write_text(json.dumps({"series": []}, indent=2), encoding="utf-8")
(data_dir / "trades.json").write_text(json.dumps([], indent=2), encoding="utf-8")
(data_dir / "run_history.json").write_text(json.dumps([], indent=2), encoding="utf-8")
(data_dir / "log_archive.json").write_text(json.dumps({"lines": []}, indent=2), encoding="utf-8")
