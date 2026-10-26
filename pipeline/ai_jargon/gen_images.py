import subprocess
import pathlib
import sys

project = pathlib.Path.cwd()
out_first = project / "pipeline" / "ai_jargon" / "out" / "first"
out_masters = project / "pipeline" / "ai_jargon" / "out" / "masters"

out_first.mkdir(parents=True, exist_ok=True)
out_masters.mkdir(parents=True, exist_ok=True)

tasks = [
    {
        "id": "tablet_ui",
        "target": out_masters / "tablet_ui.png",
        "prompt": "A 9:16 vertical cinematic close-up film still shot on Kodak Vision3 500T film with an anamorphic lens. A rugged black industrial tablet computer resting on a control room metal console desk. The glowing screen displays a sleek futuristic neon-blue audio waveform visualizer and rotating high-tech status rings on a dark cybernetic UI. No people. Realistic fluorescent lighting reflection on glass screen, subtle 35mm grain. Absolutely NO readable text, NO words, NO watermark."
    },
    {
        "id": "S01",
        "target": out_first / "S01.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot waist-up: Chen, a 32-year-old Taiwanese plant process engineer with short black hair, rectangular black glasses, wearing a dark-blue industrial plant jumpsuit with ID badge, walks briskly into the refinery control room holding a rugged black industrial tablet with a glowing screen, smiling proudly with confident bright eyes. Industrial fluorescent lighting, moody contrast, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S02",
        "target": out_first / "S02.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium close-up shot: Lao Li, a 50-year-old experienced Taiwanese refinery operator with weathered tanned face, yellow hard hat, and faded navy work jacket, holds a stainless steel vacuum thermos flask, raising one skeptical eyebrow with an amused, doubtful expression. Industrial control room background, fluorescent lighting, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S03",
        "target": out_first / "S03.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot: Ah Qiang, a 25-year-old young Taiwanese rookie plant operator with round youthful face and yellow hard hat, wearing a navy-blue work shirt, carefully holding the rugged industrial tablet with both hands extended forward toward the viewer, speaking with eager, polite and helpful eyes. Industrial control room, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S04",
        "target": out_first / "S04.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Close-up chest-up: Lao Li, a 50-year-old Taiwanese plant veteran with yellow hard hat and navy jacket, leans toward the tablet microphone, his mouth wide open speaking emphatically, right hand raised gesturing a twisting wrench motion, confident commanding loud facial expression. Industrial control room background, fluorescent lighting, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S05",
        "target": out_first / "S05.png",
        "prompt": "A 9:16 vertical cinematic extreme close-up film still shot on Kodak Vision3 500T film. Extreme close-up of a rugged industrial tablet screen displaying a glowing circular neon-blue audio waveform visualizer pulsing rapidly with circular digital rings and frequency bars in a dark sci-fi UI. No people. Subtle glass glare, fine 35mm grain. Absolutely NO readable text, NO words, NO watermark."
    },
    {
        "id": "S06",
        "target": out_first / "S06.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium close-up shot: Chen, a 32-year-old Taiwanese engineer with rectangular black glasses and dark-blue jumpsuit, staring down at the glowing tablet in his hands in absolute shock, his jaw dropped open slightly, eyes wide in stunned disbelief. Control room background with glowing monitors, dramatic moody lighting, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S07",
        "target": out_first / "S07.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Close-up dramatic shot: Lao Li, the 50-year-old plant operator with yellow hard hat, staring with eyes bulging wide in hilarious utter shock and bewilderment, mouth wide open shouting in disbelief, pointing an aggressive finger down at the tablet. Dramatic cinematic lighting, high emotional tension, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S08",
        "target": out_first / "S08.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot waist-up: Ah Qiang, a 25-year-old young Taiwanese rookie operator with yellow hard hat and navy shirt, standing in the control room biting his lower lip desperately, cheeks puffed out like a blowfish, eyes squinting, shoulders tense, struggling with all his might to stifle explosive laughter. Control room background, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S09",
        "target": out_first / "S09.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Close-up shot: Chen, the 32-year-old Taiwanese engineer with sweaty forehead and flustered expression, anxiously pushing up his slipping rectangular glasses with one hand while desperately speaking into the tablet microphone in his other hand. Industrial control room, dramatic fluorescent lighting, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S10",
        "target": out_first / "S10.png",
        "prompt": "A 9:16 vertical cinematic close-up film still shot on Kodak Vision3 500T film. Close-up shot of the rugged industrial tablet screen displaying a glowing retro-digital cool robot face wearing neon sunglasses, with glowing red and cyan digital lock icons and warning rings on a dark cybernetic UI. No people. Glass reflection, fine 35mm grain. Absolutely NO readable text, NO words, NO watermark."
    },
    {
        "id": "S11",
        "target": out_first / "S11.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot waist-up: Lao Li, the 50-year-old weathered plant veteran with yellow hard hat, laughing heartily and warmly, slapping a worn yellow pocket paper notebook down onto the metal console desk, gesturing with his hand toward the engineer off-camera with paternal amusement and wisdom. Control room setting, subtle 35mm grain. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S12",
        "target": out_first / "S12.png",
        "prompt": "A 9:16 vertical cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Close-up shot: Ah Qiang, the 25-year-old rookie operator with yellow hard hat, scratching his head under his hard hat with a completely naive, serious and genuinely puzzled expression, mouth slightly open, looking directly into the camera. Soft control room background lighting, subtle 35mm grain. Full-frame, NO text, NO watermark."
    }
]

def generate_one(t):
    target = t["target"]
    if target.exists() and target.stat().st_size > 1000:
        print(f"[{t['id']}] already exists ({target.stat().st_size} bytes). Skipping.")
        return True
    
    print(f"[{t['id']}] Generating via codex exec...")
    full_prompt = f"$imagegen {t['prompt']} Save or copy the final PNG to {target}. Do not use an API key or API fallback."
    cmd = [
        "codex.cmd", "exec",
        "--skip-git-repo-check",
        "--sandbox", "workspace-write",
        "--cd", str(project),
        full_prompt
    ]
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if target.exists() and target.stat().st_size > 1000:
            print(f"[{t['id']}] SUCCESS! Size: {target.stat().st_size} bytes")
            return True
        else:
            print(f"[{t['id']}] Warning: Target not found at {target}")
            print("Codex stdout tail:", res.stdout[-400:] if res.stdout else "")
            print("Codex stderr tail:", res.stderr[-400:] if res.stderr else "")
            return False
    except Exception as e:
        print(f"[{t['id']}] Error running codex: {e}")
        return False

if __name__ == "__main__":
    target_id = sys.argv[1] if len(sys.argv) > 1 else None
    for task in tasks:
        if target_id and task["id"] != target_id:
            continue
        generate_one(task)
