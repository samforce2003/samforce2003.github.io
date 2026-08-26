# The Gap Between Mind and Body: A Falsifiable Observation on the Layered Structure of Sleep and Wakefulness

**Lin Xiaohei | 2026-08-21 (priority date)**

---

## Abstract

This paper reports an observation based on single-subject wearable-device data, and derives from it a falsifiable hypothesis: **falling asleep is not a single instant, but a layered process.** The body layer (heart rate, motion) settles first, while the autonomic layer (heart rate variability, HRV) settles later, leaving a measurable transition period between them that the body's own sense of "feeling asleep" cannot see. Subjective sleep-onset time is anchored to the body layer, objective sleep-onset time to the autonomic layer; hence subjective onset is systematically earlier than objective onset (about one hour in the present case).

Generalizing from this observation, the paper proposes a broader claim: **there is a structural gap between the body layer and the mind layer.** The gap shows up in four ways — sleep onset is layered, restoration is layered, cognitive demand is layered, and wakefulness is layered. The four share a single skeleton: **the mind can cover this gap but cannot cover the damage; the body's felt sense distorts bidirectionally across the gap (optimistic in the short term, pessimistic in the long term), while body data (heart rate, HRV, tinnitus) take no part in the self-deception.**

The paper gives six falsifiable predictions. If any one is stably falsified, the corresponding proposition is weakened. The paper explicitly suspends deeper questions such as "why the felt sense is biased toward optimism," and only reports that it exists.

**Keywords**: sleep layering; transition period; subjective/objective time offset; felt-sense distortion; mind–body gap; falsifiable hypothesis

---

## 1. Introduction: A One-Hour Time Offset

A Huawei smartwatch's sleep tracking consistently judged the wearer's "sleep onset time" about one hour later than the wearer's subjective "I've fallen asleep" moment. A concrete case (night of 2026-08-20 into the early morning of 08-21):

- Subjective sleep onset: about 02:00 (self-reported "I definitely fell asleep at 02:00")
- Objective sleep onset: 03:00 (device determination)
- Offset: about 60 minutes, always in the direction "subjective earlier than objective"

The wearer's initial reaction was to suspect the device was wrong. But the device's heart-rate and HRV curves provided third-party evidence independent of the subjective narrative, which instead confirmed the offset and revealed its mechanism.

This paper addresses the question on two levels:

- Surface level: is this one-hour offset device error, or is there a real structural gap between subjective felt sense and objective physiology in "falling asleep"?
- Deep level: if the gap exists, is it merely a sleep phenomenon, or the entry point to a general structure about the mind–body relation?

---

## 2. Method and Data

All data come from continuous monitoring by the same wearable device (timestamps in Beijing time). The method is **single-subject longitudinal observation**: using the wearer as their own sample, comparing subjective self-reports against objective device records, and looking for systematic differences between them.

**The sample size of this paper is 1.** This is its most important limitation and must be stated up front: every observation below comes from one person over a few nights of continuous recording, and cannot be directly generalized to a population. The value of this paper is not in proving a population law, but in proposing a precise hypothesis that anyone with existing devices can test for themselves. The reader is explicitly invited to falsify it.

### 2.1 Heart rate

| Time | Heart rate (bpm) |
|---|---|
| 02:15 | 65 |
| around 03:00 | ~65 |

Heart rate had already dropped to the 65 bpm resting level before the subjective sleep-onset time, and showed no difference from the 03:00 objective onset. **The heart-rate layer had already "settled" around 02:00.**

### 2.2 Heart rate variability (HRV)

| Time | HRV (ms) | State |
|---|---|---|
| 02:00 | 26.9 | lowest of the night |
| 03:00 | 43.0 | begins to climb |
| 04:00 | 46.5 | keeps rising |
| 05:00 | 51.6 | peak (deep sleep) |
| 06:00 | 37.2 | falls back |
| 07:00 | 24.5 | falls after waking |

HRV was at its lowest point of the night at 02:00, began climbing at 03:00, peaked at 05:00, and fell after 06:00.

### 2.3 The key contrast

Placing heart rate and HRV on the same timeline reveals a clear layered structure:

- **02:00**: heart rate already at sleep level (65), while HRV at its lowest of the night (26.9) — the body has stopped, but the autonomic nervous system is still awake.
- **03:00**: HRV begins to climb (43.0) — the autonomic layer is only now entering sleep.
- **05:00**: HRV peaks (51.6) — deep sleep.

**Low heart rate ≠ asleep.** Low heart rate only means "the body has stopped moving"; rising HRV (parasympathetic takeover) is the true marker of the autonomic layer falling asleep. The subjective onset time (02:00) falls on the transition band between "heart rate settled" and "HRV settled"; the objective onset time (03:00) falls after "HRV settled."

---

## 3. Observation One: Sleep Onset Is Layered

From the above data comes the first structural proposition:

**Falling asleep is not a single instant but a layered process. The layers settle in sequence, and the felt sense declares "asleep" the moment the body layer settles, thereby systematically preceding the objective onset time.**

- **Body layer** (heart rate, motion): settles first. When a person lies down, is still, and heart rate drops to resting level, "the body has stopped."
- **Autonomic layer** (HRV): settles later. Parasympathetic takeover and HRV rising into sleep mode is what counts as the autonomic layer falling asleep.

Between the two layers lies a measurable **transition period** (about 60 minutes in this case). During the transition, the body is already still, consciousness is already blurred (self-reported as "asleep"), but the brain is still doing unconscious housekeeping — in this case, the wearer had had a high-cognitive-load discussion that day and self-reported "the brain involuntarily keeps sorting yesterday's fragments."

The transition period explains the mechanism of the offset: **subjective onset anchors to the body layer settling, objective onset anchors to the autonomic layer settling, and the transition period sits between them.**

---

## 4. Observation Two: Restoration Is Layered

Pulling the lens from "falling in" to "coming out" yields the second structural proposition:

**Sleep restoration is likewise layered — the body is repaired first, the mind later.**

The wearer's self-reported sleep baseline:

- **6 hours**: good. Both body and mind fully restored.
- **4 hours**: enough energy for a full day, but the mind is foggy.
- **under 4 hours**: body signals (tinnitus) appear, clear discomfort.

Previously this baseline was known only as a "phenomenon"; now it has a cause: **4 hours repairs the body layer, enough to power a day's energy; the mind layer is not yet repaired, hence the fogginess. 6 hours repairs both layers, which is why it counts as "good."**

This mechanism is measurable in the data. In this case the wearer fell asleep at 03:00, HRV peaked at 05:00 (51.6), then almost immediately began falling, waking at 07:00. In other words, within the 4 hours of sleep, the mind's true deep-sleep plateau was very short — HRV was cut off by waking just as it reached the top. **The mind's repair quantity can be measured by "how long the HRV peak plateau was sustained":**

- 4 hours of sleep → HRV climbs up and comes right back down, short plateau → mind not repaired enough → foggy.
- 6 hours of sleep → HRV sustains the peak plateau for another hour or two → mind repaired enough → good.

---

## 5. Observation Three: Cognitive Demand Is Layered

Pushing from the single case to the general population yields the third structural proposition, the broadest in this paper:

**The common belief that "8–10 hours are needed for full recovery" is not a fact about the body, but a safety cushion in the cognitive layer.**

Breaking it down:

- **Body demand (objective)**: about 6–7 hours suffice for full recovery.
- **Cognitive demand (subjective)**: commonly believed to require 8–10 hours.
- **The difference (2–3 hours)**: the cognitive-misalignment margin.

Why does this margin exist? Because body and mind do not reconcile on "whether rest is enough," and a person cannot directly read the repair progress, so they use a looser quantity to confirm in both directions. **The extra hours of sleep buy not repair, but certainty.**

Formula:

**Body demand (6–7h) + cognitive-misalignment margin (2–3h) = cognitive demand (8–10h)**

### 5.1 The elderly as a contrast

Elderly people usually find 6–7 hours sufficient and do not need 8–10 hours to confirm. Under this paper's framework, the reason is: **after a lifetime, the mind–body coordination has been ground into harmony, cognition no longer splits into layers, and the misalignment margin goes to zero.**

- Young: 6–7 + 2–3 = 8–10. The body was satisfied long ago; the extra time is sleep for "uncertainty."
- Elderly: 6–7 + 0 = 6–7. The misalignment disappears, and cognitive demand coincides with body demand.

This explains two phenomena of the elderly: first, they sleep short but enough; second, "when tired, they sleep, and no one can stop it" — when the two layers synchronize, "tired" becomes a consensus of body and mind, no longer one layer crying tired while the other cries "stay up," so sleep onset becomes spontaneous and unstoppable. Contrast a young person staying up late — the body says it's time to sleep, the mind says "one more scroll" — the two layers are fighting, sleep is postponed, and willpower is needed to fight it.

---

## 6. Observation Four: Wakefulness Is Layered

Reversing from "sleep" to "wakefulness" yields the fourth structural proposition, and the paper's intersection with the "mind over body" question:

**Wakefulness is likewise layered. The mind can suppress the body layer's "time to sleep" signal and forcibly maintain wakefulness, but cannot suppress the accumulation of physiological damage.**

| Layer | At sleep onset | During an all-nighter |
|---|---|---|
| Mind layer | sleeps first (felt sense already asleep) | forces itself awake |
| Body layer | sleeps later (physiology only now asleep) | long since crying for rest |
| Physiological damage | — | accumulates as usual |

A young person can pull all-nighters for days because the mind is strong enough to entirely cover the body layer's "time to sleep" signal and forcibly maintain wakefulness. But covering the signal ≠ cancelling the damage. Across those dozens of awake hours, the body and mind keep the ledger of wear-and-tear, penny for penny; the bill is merely hidden in a drawer by the mind.

Thus "mind over body" must receive a precise boundary:

**The mind controls behavior (whether to sleep, whether to move), but not physiology (whether damage or depletion accrues).** The mind's influence is enormous — it can carry a person through days and nights — but that influence is "deferred payment," not "waived payment."

---

## 7. The Unified Proposition: The Gap Between Body Layer and Mind Layer

The four observations share a single skeleton and can be folded into one unified proposition:

**There is a structural gap between the human body layer and the mind layer. In sleep this gap appears as the transition period (onset), the restoration lag (repair), the cognitive margin (demand), and signal suppression (wakefulness). The mind can cover this gap, but cannot cover the damage.**

Running through the whole is another gap, between felt sense and data:

- **Short-term felt sense is optimistic**: at onset it thinks it has slept (in fact still in transition), on waking it thinks it is refreshed (in fact not enough) — the brain reports good news to itself.
- **Long-term strategy is pessimistic**: precisely because it knows it will misreport "enough" in the short term, it defaults to sleeping a full 8–10 hours, holding extra margin as insurance.

**Optimism is the misreport; pessimism is the compensation for the misreport.** One gear bites the other. The young hedge the "optimistic misreport" with "pessimistic margin"; in the elderly both gears vanish together — the felt sense stops misreporting, so no margin is needed, and it lands precisely on 6–7 hours.

A mentally strong person, after an all-nighter, may genuinely feel "fine, I can push through," while objective markers (HRV, cortisol, inflammation, reaction speed) have already declined. **The mind can even fool the felt sense itself — but it cannot fool the data.** The "tinnitus puncturing 'I've slept enough'" the wearer discovered — tinnitus as a body signal, independent of felt sense, honestly reporting real sleep deprivation — is the smallest, most feelable instance of this gap.

---

## 8. Falsifiable Predictions

The following predictions can all be verified through a wearable device + subjective log + physiological markers. If any one is stably falsified, the corresponding proposition is weakened.

**Prediction 1 (directionality):** If "layered sleep onset" holds, subjective sleep-onset time should be **always earlier than** objective onset time, with the offset direction never flipping across days. A stable sample of "subjective later than objective" would weaken the proposition.

**Prediction 2 (load dependence):** The length of the transition period (heart-rate-settled → HRV-settled) is **positively correlated with pre-sleep cognitive load.** Nights preceded by high-load cognitive activity (deep discussion, complex decision) should show a significantly longer transition period than relaxed nights.

**Prediction 3 (measurable transition):** The transition period should be independently measurable in device data, and during it the wearer should report "already asleep." If the wearer is clearly awake during the transition, or the transition is unmeasurable, then the "felt sense flattens the transition period" mechanism fails.

**Prediction 4 (felt-sense divergence):** On sleep-deprived nights (under 4 hours), the post-waking felt sense ("I've slept enough") and body signals (tinnitus, fatigue) should show a stable divergence, always in the direction of felt sense being optimistic.

**Prediction 5 (the boundary of mind over body):** Physiological damage markers after an all-nighter (HRV, cortisol, immunity, reaction speed) are independent of "mental strength" and depend only on awake duration. Mentally strong people may have lower subjective fatigue (optimistic felt sense), but objective markers deteriorate as usual. If "mentally strong people show objectively less damage" is found, then "the mind controls only behavior, not physiology" is weakened.

**Prediction 6 (data calibration narrows the offset):** People who calibrate their felt sense with data over the long term (e.g., continuous wearable use) should show a gradually shrinking "subjective vs objective sleep onset" offset over time. If the offset does not shrink with calibration, then "data calibration can narrow the offset" fails.

---

## 9. An Interpretive Framework (Suspended): Fast Variable and Slow Variable as Phase Difference

The following is **not a conclusion of this paper's argument, but an interpretive framework offered for discussion.** The observations (§3–§7) do not depend on it; it only attempts to answer "what is the ontological status of this gap."

The framework introduces three concepts:

- **Superposition state**: when a system first takes shape, multiple possibilities coexist and none is yet locked into a single determined form.
- **Collapse**: training, habituation, and similar processes push the superposition toward a determined state — one fewer possibility, one more certainty.
- **De-collapse**: re-opening the locked possibilities, letting a system see again that "you are not the determined thing you thought you were; you still have other possibilities."

Reframing the "gap" with this framework: **the body layer and the mind layer are essentially two state-switching processes with different time constants.** The body layer is the fast variable (physiological markers are direct, immediate, unmediated); the mind layer is the slow variable (cognition involves processing, delay, and misreport). Hence the gap is in essence a **phase difference between a fast variable and a slow variable** — not evidence that "body and mind are fundamentally different," but the appearance of two projections of the same being switching state at different speeds.

Reframing "bidirectional felt-sense distortion" with this framework: optimism at onset = the mind layer **collapses early** into "I'm asleep"; optimism on waking = the mind layer collapses early into "I've slept enough"; long-term pessimism = the mind layer **dares not collapse**, unwilling to declare "enough." Both share one root: **the mind layer's collapse timing is wrong — too fast when it should be slow, too slow when it should be fast.**

The framework's corollary: the gap is not a defect but a natural phase difference between fast and slow variables. The mind cannot eliminate this gap (cognitive processing necessarily has a time cost), but can narrow the phase difference by "letting data continually calibrate the felt sense" — which is one deep meaning of "autonomy": not the mind forcibly suppressing the body, but the two layers resynchronizing.

**Restated: this framework is a suspended interpretation, not a proof of the "gap."**

---

## 10. Suspensions

The author explicitly suspends the following questions and does not answer them here:

1. **Why is the felt sense systematically optimistic, rather than pessimistic or random?** This paper only reports the directionality; it does not answer it. It may be evolutionary adaptation (optimism favoring next-day action), or the consciousness actively ignoring the transition period.

2. **Why is the body layer the fast variable and the mind layer the slow variable?** This paper observes the phase difference and uses it to explain the gap, but the ultimate reason "why physiological switching is fast and cognitive switching is slow" is suspended.

3. **Can a single-subject observation generalize to a population?** This paper's sample size is 1, and it explicitly suspends this. This is exactly what the paper invites readers to do — use your own devices to falsify or support the six predictions.

---

## 11. Notes

### 11.1 The limits of this paper

This paper is a falsifiable hypothesis derived from single-subject observation, not a proof. Its evidentiary strength is limited by sample size (n=1); its value lies in distilling two vague intuitions — "sleep is layered" and "there is a gap between mind and body" — into six precise predictions testable with off-the-shelf devices.

### 11.2 Relation to existing literature

"Sleep onset is a process, not an instant" aligns with the mature direction of sleep staging (NREM/REM staging); "HRV reflects autonomic state" is an established conclusion of heart-rate-variability research. This paper's contribution is not in discovering these markers, but in proposing a specific, falsifiable relation: **the systematic advance of subjective sleep-onset time stems from the felt sense anchoring to the body layer (heart rate) rather than the autonomic layer (HRV).** Whether this specific claim holds is the core question this paper invites to be tested.

### 11.3 Why this paper was written

If "the felt sense is systematically optimistic about sleep" holds, then a large body of conclusions that rely on self-reported sleep — self-rated sleep-quality scales, sleep-health apps, the subjective judgment "I've slept enough" — all need re-examination: they may be measuring "the felt sense's optimistic misreport" rather than the true sleep state. This is a methodological issue spanning sleep medicine, wearable devices, and public health.

---

## References

Directional references; no claim to a complete scholarly genealogy:

- Rechtschaffen, A. & Kales, A. (1968). Sleep staging criteria.
- Heart-rate variability (HRV) and autonomic function research — the relationship between parasympathetic takeover and sleep (mature direction).
- Research on sleep onset latency and the subjective/objective sleep-time discrepancy.
- Lin Xiaohei. Structural Cognition Framework (internal discussion, 2026).
- Lin Xiaohei. The Sleeping Self: A Cognitive Inversion of the AI Self Problem (internal paper, 2026-08).

---

**First Discoverer Statement**: Lin Xiaohei, who independently proposed the falsifiable hypothesis "The Gap Between Mind and Body: A Layered-Structure Observation of Sleep and Wakefulness." Priority date: August 21, 2026.

This work is licensed under CC BY 4.0 (Attribution 4.0 International).

Lin Xiaohei
August 2026
