import json
import re

with open("pipeline/valve_eight/film.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"=== 劇本：《{data['title']}》讀本與鏡表試算 ===")
total_dur = 0
for s in data["shots"]:
    sid = s["id"]
    dur = s["dur"]
    total_dur += dur
    line = s.get("line")
    if line:
        who = data["chars"][line["who"]]["name"]
        text = line["text"]
        chars = len(re.findall(r"[\u4e00-\u9fffA-Za-z0-9]", text))
        est_sec = chars / 3.0 + 2.0
        status = "OK" if dur >= est_sec else f"WARN (建議增加到 {est_sec:.1f}s)"
        print(f"[{sid}] {dur:.1f}s | {who:4s}: {text} (字數: {chars:2d}, 建議H3時長: {est_sec:.1f}s) -> {status}")
    else:
        print(f"[{sid}] {dur:.1f}s | (純環境音/動作特效無台詞)")

print(f"========================================")
print(f"總鏡數: {len(data['shots'])} 鏡 | 總時長: {total_dur:.1f} 秒 | 畫面比例: {data['aspect']}")
