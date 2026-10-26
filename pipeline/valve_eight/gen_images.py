import subprocess
import pathlib
import sys

project = pathlib.Path.cwd()
out_first = project / "pipeline" / "valve_eight" / "out" / "first"
out_masters = project / "pipeline" / "valve_eight" / "out" / "masters"

out_first.mkdir(parents=True, exist_ok=True)
out_masters.mkdir(parents=True, exist_ok=True)

tasks = [
    {
        "id": "control",
        "target": out_masters / "control.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Inside the central control room of a Taiwanese oil refinery plant during a critical emergency. Long curved control consoles with multiple glowing monitors displaying flashing red danger graphics and alarm warnings. Flashing crimson rotating emergency beacon light casting dramatic red streaks across the metal desks and ceiling. No people. Clean cinematic composition, realistic heavy industrial atmosphere. Full-frame, NO readable text, NO words, NO watermark."
    },
    {
        "id": "pipe_corridor",
        "target": out_masters / "pipe_corridor.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Inside a heavy industrial refinery pipeline hall. Massive interconnected silver steel pipes, overhead catwalks, white steam hissing faintly from high-pressure flange joints creating atmospheric mist. Prominently mounted on a central pipe is a huge heavy red cast-iron manual handwheel valve, flanked by an analog pressure dial. Moody cinematic industrial lighting with deep cool shadows and warm cage lights. No people. Full-frame, NO readable text, NO words, NO watermark."
    },
    {
        "id": "S01",
        "target": out_first / "S01.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot waist-up: Chen, a 32-year-old Taiwanese plant process engineer with short black hair and rectangular black glasses, wearing a dark-blue industrial jumpsuit, clutches a handheld radio walkie-talkie with trembling hands, staring in sheer terror at flashing red control monitors, shouting with urgent panic. Flashing crimson emergency lighting, moody shadows, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S02",
        "target": out_first / "S02.png",
        "prompt": "A 16:9 widescreen horizontal cinematic close-up film still shot on Kodak Vision3 500T film. Close-up of a massive rugged red cast-iron handwheel valve mounted on an industrial steel pipeline. A circular brass analog pressure gauge next to it has its needle trembling violently at the red maximum danger limit. Hissing white steam leaks from the pipe flange. Atmospheric dramatic lighting, water droplets condensing on metal. No people. Full-frame, NO text, NO watermark."
    },
    {
        "id": "S03",
        "target": out_first / "S03.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot: Ah Qiang, a 25-year-old young Taiwanese rookie plant operator with round youthful face and yellow hard hat, wearing a navy-blue work shirt, rushes forward and firmly grips the large red valve handwheel on the industrial pipe, pulling with all his upper body strength, face straining intensely amidst swirls of white steam. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S04",
        "target": out_first / "S04.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Tight intense close-up shot: Ah Qiang, a 25-year-old Taiwanese rookie operator with yellow hard hat, face flushed deep red, sweat pouring down his temples, teeth clenched hard, veins bulging across his neck and forehead as he strains desperately against the unyielding red valve, eyes filled with grit and struggle. Industrial pipe background with hissing steam, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S05",
        "target": out_first / "S05.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium close-up shot: Chen, the 32-year-old engineer with rectangular glasses and blue jumpsuit, screams desperately into his walkie-talkie in the red-lit control room, his face pale with terror as digital warning sirens flash crimson light across his sweaty face. High emotional tension, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S06",
        "target": out_first / "S06.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Low-angle heroic medium shot: Lao Li, a 50-year-old experienced Taiwanese plant veteran with weathered tanned face, yellow hard hat, and faded navy-blue work jacket, strides powerfully through heavy steam fog in the industrial corridor, carrying a long heavy steel extension cheater pipe over his right shoulder, eyes blazing with fierce veteran resolve. Moody cinematic lighting, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S07",
        "target": out_first / "S07.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Dynamic medium close-up shot: Lao Li with yellow hard hat skillfully jams a thick galvanized steel cheater bar through the spokes of the stubborn red valve handwheel on the pipe, locking it into a powerful leverage position. Sparks of determination in his eyes, steam billowing around, heavy industrial textures. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S08",
        "target": out_first / "S08.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot: Lao Li, the 50-year-old veteran with yellow hard hat and navy jacket, holds the end of the long steel lever bar with one calloused hand, pointing sharply at the bar with the other, shouting commanding instructions to Ah Qiang with fiery leadership in the steamy corridor. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S09",
        "target": out_first / "S09.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium close-up shot: Ah Qiang, the 25-year-old rookie with yellow hard hat, his fear transformed into blazing adrenaline, steps up beside the lever bar, planting both gloved hands firmly onto the steel pipe with fierce resolve, shouting with determined eyes. Steamy industrial pipe background, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S10",
        "target": out_first / "S10.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Wide cinematic two-shot: Lao Li and Ah Qiang side-by-side in the industrial pipeline hall, both throwing their entire body weight downward onto the long steel lever bar, facial veins and arm muscles bulging, screaming at the top of their lungs in unison amidst swirling steam mist. High action tension, dramatic rim lighting, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S11",
        "target": out_first / "S11.png",
        "prompt": "A 16:9 widescreen horizontal cinematic close-up macro film still shot on Kodak Vision3 500T film. The heavy red valve handwheel on the pipe violently rotating half a turn with metallic motion blur. Behind it, a massive jet of high-pressure white steam erupts out of the relief exhaust in a glorious plume. No people. Industrial steel piping, dramatic backlighting through steam mist. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S12",
        "target": out_first / "S12.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Cinematic medium shot: In the pipeline corridor where emergency lights have returned to calm green, Lao Li sits resting against a steel pipe support, panting heavily, wiping sweat from his forehead with a grease-stained glove, grinning proudly with veteran swagger and giving an approving thumbs-up. Atmospheric post-crisis lighting, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    {
        "id": "S13",
        "target": out_first / "S13.png",
        "prompt": "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Cinematic medium close-up shot: Ah Qiang, the 25-year-old rookie operator with yellow hard hat, sits leaning against a steel pipe in the green-lit corridor, face sweaty with light grease smudges. He wipes his brow with the back of his gloved wrist, breathing a heavy sigh of relief, then turns to gaze off-camera toward Lao Li with bright glowing eyes full of pure awe, respect, and a radiant, starry-eyed admiring smile. Full-frame, NO readable text, NO watermark."
    }
]

def generate_one(t):
    target = t["target"]
    if target.exists() and target.stat().st_size > 1000:
        print(f"[{t['id']}] already exists ({target.stat().st_size} bytes). Skipping.", flush=True)
        return True
    
    print(f"[{t['id']}] Generating via codex exec...", flush=True)
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
            print(f"[{t['id']}] SUCCESS! Size: {target.stat().st_size} bytes", flush=True)
            return True
        else:
            print(f"[{t['id']}] Warning: Target not found at {target}", flush=True)
            print("Codex stdout tail:", res.stdout[-400:] if res.stdout else "", flush=True)
            print("Codex stderr tail:", res.stderr[-400:] if res.stderr else "", flush=True)
            return False
    except Exception as e:
        print(f"[{t['id']}] Error running codex: {e}", flush=True)
        return False

if __name__ == "__main__":
    target_id = sys.argv[1] if len(sys.argv) > 1 else None
    for task in tasks:
        if target_id and task["id"] != target_id:
            continue
        generate_one(task)
