with open("pipeline/valve_eight/make_film.py", "r", encoding="utf-8") as f:
    text = f.read()

target = 'a = load(l["file"]); s0 = int(l["film_start"] * SR); voice[s0:s0 + len(a)] += a[: n - s0]'
replacement = '''a = load(l["file"])
            s0 = int(l["film_start"] * SR)
            a_start = max(0, -s0)
            v_start = max(0, s0)
            a_chunk = a[a_start:a_start + max(0, n - v_start)]
            v_end = v_start + len(a_chunk)
            if v_end > v_start and len(a_chunk) > 0:
                voice[v_start:v_end] += a_chunk'''

assert target in text, "Target string not found"
text = text.replace(target, replacement)

# 修正 duck 切片上限
duck_target = 'duck[max(0, int((l["film_start"] - 0.25) * SR)):int((l["film_end"] + 0.35) * SR)] = under'
duck_replacement = 'duck[max(0, int((l["film_start"] - 0.25) * SR)):min(n, int((l["film_end"] + 0.35) * SR))] = under'
text = text.replace(duck_target, duck_replacement)

# 修正 amb 貼入
amb_target = 'a = load(r["amb"])[int(r["src_in"] * SR):int(r["src_out"] * SR)]\n            s0 = int(r["start"] * SR); amb_[s0:s0 + len(a)] += a[: n - s0]'
amb_replacement = '''a = load(r["amb"])[int(r["src_in"] * SR):int(r["src_out"] * SR)]
            s0 = int(r["start"] * SR)
            a_start = max(0, -s0)
            v_start = max(0, s0)
            a_chunk = a[a_start:a_start + max(0, n - v_start)]
            v_end = v_start + len(a_chunk)
            if v_end > v_start and len(a_chunk) > 0:
                amb_[v_start:v_end] += a_chunk'''

if amb_target in text:
    text = text.replace(amb_target, amb_replacement)
elif amb_target.replace("\n", "\r\n") in text:
    text = text.replace(amb_target.replace("\n", "\r\n"), amb_replacement.replace("\n", "\r\n"))

with open("pipeline/valve_eight/make_film.py", "w", encoding="utf-8") as f:
    f.write(text)

print("make_film.py audio slicing fixed successfully!")
