param(
    [string]$TargetId = ""
)

$project = (Get-Location).Path
$outFirst = Join-Path $project "pipeline\valve_eight\out\first"
$outMasters = Join-Path $project "pipeline\valve_eight\out\masters"

New-Item -ItemType Directory -Force -Path $outFirst | Out-Null
New-Item -ItemType Directory -Force -Path $outMasters | Out-Null

$items = @(
    @{
        id = "control"
        target = Join-Path $outMasters "control.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Inside the central control room of a Taiwanese oil refinery plant during a critical emergency. Long curved control consoles with multiple glowing monitors displaying flashing red danger graphics and alarm warnings. Flashing crimson rotating emergency beacon light casting dramatic red streaks across the metal desks and ceiling. No people. Clean cinematic composition, realistic heavy industrial atmosphere. Full-frame, NO readable text, NO words, NO watermark."
    },
    @{
        id = "pipe_corridor"
        target = Join-Path $outMasters "pipe_corridor.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Inside a heavy industrial refinery pipeline hall. Massive interconnected silver steel pipes, overhead catwalks, white steam hissing faintly from high-pressure flange joints creating atmospheric mist. Prominently mounted on a central pipe is a huge heavy red cast-iron manual handwheel valve, flanked by an analog pressure dial. Moody cinematic industrial lighting with deep cool shadows and warm cage lights. No people. Full-frame, NO readable text, NO words, NO watermark."
    },
    @{
        id = "S01"
        target = Join-Path $outFirst "S01.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot waist-up: Chen, a 32-year-old Taiwanese plant process engineer with short black hair and rectangular black glasses, wearing a dark-blue industrial jumpsuit, clutches a handheld radio walkie-talkie with trembling hands, staring in sheer terror at flashing red control monitors, shouting with urgent panic. Flashing crimson emergency lighting, moody shadows, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S02"
        target = Join-Path $outFirst "S02.png"
        prompt = "A 16:9 widescreen horizontal cinematic close-up film still shot on Kodak Vision3 500T film. Close-up of a massive rugged red cast-iron handwheel valve mounted on an industrial steel pipeline. A circular brass analog pressure gauge next to it has its needle trembling violently at the red maximum danger limit. Hissing white steam leaks from the pipe flange. Atmospheric dramatic lighting, water droplets condensing on metal. No people. Full-frame, NO text, NO watermark."
    },
    @{
        id = "S03"
        target = Join-Path $outFirst "S03.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot: Ah Qiang, a 25-year-old young Taiwanese rookie plant operator with round youthful face and yellow hard hat, wearing a navy-blue work shirt, rushes forward and firmly grips the large red valve handwheel on the industrial pipe, pulling with all his upper body strength, face straining intensely amidst swirls of white steam. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S04"
        target = Join-Path $outFirst "S04.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Tight intense close-up shot: Ah Qiang, a 25-year-old Taiwanese rookie operator with yellow hard hat, face flushed deep red, sweat pouring down his temples, teeth clenched hard, veins bulging across his neck and forehead as he strains desperately against the unyielding red valve, eyes filled with grit and struggle. Industrial pipe background with hissing steam, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S05"
        target = Join-Path $outFirst "S05.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium close-up shot: Chen, the 32-year-old engineer with rectangular glasses and blue jumpsuit, screams desperately into his walkie-talkie in the red-lit control room, his face pale with terror as digital warning sirens flash crimson light across his sweaty face. High emotional tension, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S06"
        target = Join-Path $outFirst "S06.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Low-angle heroic medium shot: Lao Li, a 50-year-old experienced Taiwanese plant veteran with yellow hard hat and navy jacket, strides powerfully through heavy steam fog in the industrial corridor, carrying a long hollow steel extension cheater pipe over his shoulder and holding a shiny steel F-type valve wheel wrench with two parallel hooked jaws in his hand, eyes blazing with fierce veteran resolve. Moody cinematic lighting, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S07"
        target = Join-Path $outFirst "S07.png"
        prompt = "A 16:9 widescreen horizontal cinematic close-up shot on Kodak Vision3 500T film. Lao Li with yellow hard hat skillfully clamps the dual parallel hooked prongs of a heavy steel F-type valve wrench firmly onto the outer circular rim of the massive RED cast-iron valve handwheel on the horizontal steel pipeline. He slides a hollow silver steel extension sleeve pipe over the handle of the F-wrench to extend leverage. Sparks of determination in his eyes, steam billowing around. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S08"
        target = Join-Path $outFirst "S08.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium shot: In the steamy pipeline corridor, the steel F-type valve wrench is clamped tightly onto the outer circular rim of the massive round RED cast-iron valve handwheel on the pipe. Lao Li, the 50-year-old veteran with yellow hard hat and navy jacket, firmly grips the long hollow extension pipe that is sleeved over the handle of the F-wrench, pointing with his other hand and shouting commanding instructions to Ah Qiang with fiery leadership. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S09"
        target = Join-Path $outFirst "S09.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Medium close-up shot: Beside the identical massive round RED cast-iron valve handwheel with the steel F-wrench clamped securely onto its outer rim, Ah Qiang, the 25-year-old rookie with yellow hard hat, his fear transformed into blazing adrenaline, steps up and firmly plants both gloved hands onto the long silver extension pipe sleeved over the F-wrench handle, shouting with burning resolve. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S10"
        target = Join-Path $outFirst "S10.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Wide cinematic two-shot: Lao Li and Ah Qiang side-by-side at the massive round RED cast-iron valve handwheel on the horizontal industrial pipeline. The steel F-type valve wrench is hooked tightly onto the handwheel's outer circular rim, with the long silver extension sleeve pipe extending outward. Both men throw their entire body weight downward onto the extension pipe, muscles and veins bulging, screaming at the top of their lungs in unison amidst swirling white steam mist. High action tension, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S11"
        target = Join-Path $outFirst "S11.png"
        prompt = "A 16:9 widescreen horizontal cinematic close-up macro film still shot on Kodak Vision3 500T film. The heavy red valve handwheel on the pipe violently rotating half a turn with metallic motion blur. Behind it, a massive jet of high-pressure white steam erupts out of the relief exhaust in a glorious plume. No people. Industrial steel piping, dramatic backlighting through steam mist. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S12"
        target = Join-Path $outFirst "S12.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Cinematic medium shot: In the pipeline corridor where emergency lights have returned to calm green, Lao Li sits resting against a steel pipe support, panting heavily, wiping sweat from his forehead with a grease-stained glove, grinning proudly with veteran swagger and giving an approving thumbs-up. Atmospheric post-crisis lighting, subtle 35mm grain. Full-frame, NO readable text, NO watermark."
    },
    @{
        id = "S13"
        target = Join-Path $outFirst "S13.png"
        prompt = "A 16:9 widescreen horizontal cinematic film still shot on Kodak Vision3 500T film with an anamorphic lens. Cinematic medium close-up shot: Ah Qiang, the 25-year-old rookie operator with yellow hard hat, sits leaning against a steel pipe in the green-lit corridor, face sweaty with light grease smudges. He wipes his brow with the back of his gloved wrist, breathing a heavy sigh of relief, then turns to gaze off-camera toward Lao Li with bright glowing eyes full of pure awe, respect, and a radiant, starry-eyed admiring smile. Full-frame, NO readable text, NO watermark."
    }
)

foreach ($item in $items) {
    if ($TargetId -ne "" -and $item.id -ne $TargetId) {
        continue
    }
    if ((Test-Path $item.target) -and ((Get-Item $item.target).Length -gt 1000)) {
        Write-Host "[$($item.id)] Already exists: $($item.target)" -ForegroundColor DarkGray
        continue
    }
    Write-Host "[$($item.id)] Generating image via Codex CLI..." -ForegroundColor Cyan
    $fullPrompt = '$imagegen ' + $item.prompt + ' Save or copy the final PNG to ' + $item.target + '. Do not use an API key or API fallback.'
    $null | codex exec --skip-git-repo-check --sandbox workspace-write --cd $project $fullPrompt
    if ((Test-Path $item.target) -and ((Get-Item $item.target).Length -gt 1000)) {
        Write-Host "[$($item.id)] Successfully generated: $($item.target)" -ForegroundColor Green
    } else {
        Write-Host "[$($item.id)] Failed to generate!" -ForegroundColor Red
    }
}
