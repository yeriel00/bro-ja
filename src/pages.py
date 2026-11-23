"""Page content. Copy follows the AHS_EMP Website Content Model (v2, Nov 23); layout and
components follow the interior-page design artifact."""
from parts import *  # noqa: F401,F403
from parts import ARROW, Q, Q_HL, PHOTO, URL
from hero_cells import face_grid
from resources import LIBRARY_JSON
from social import SOCIAL

OVERCOME = ("Hutchinson S, Nicholson RA, Vargas B, et al. Seeking care, diagnosis, and acute prescription for migraine among those "
            "with headache-related disability: results of the OVERCOME study. Headache. 2020;60(S1):132–133. Final claim mapping pending.")
AHS_STUDY = ("Hyden C, Moskowitz A, Seng E. The AHS Healthcare Professional Awareness Campaign to Combat Migraine Stigma: "
             "Formative Research Phase Preliminary Report. 2026.")


# =====================================================================================
# 0.0 HOME
# =====================================================================================
def home():
    stats = "".join([
        stat("#1", f"cause of disability worldwide for people under 50.{sup(4)}"),
        stat("9 in 10", f"can’t work or function normally when symptoms hit.{sup(5)}"),
        stat("113M", f"workdays lost to migraine each year in the U.S.{sup(6)}"),
        stat("42%", f"live with moderate or greater migraine-related disability.{sup(7)}"),
        stat("8 in 10", f"have symptoms beyond head pain, like nausea, fatigue, and sensitivity to light and sound.{sup(8)}"),
        stat("1 in 2", f"people eventually diagnosed with migraine didn’t know they had it.{sup(9)}"),
    ])
    refs = [
        "Citation pending — U.S. migraine prevalence: more than 40 million.",
        OVERCOME,
        "Citation pending — World Health Organization: migraine and global disability.",
        "Citation pending — Leading cause of disability in people under 50.",
        "Citation pending — Ability to work or function during symptoms.",
        "Citation pending — Annual U.S. workdays lost to migraine.",
        "Citation pending — Moderate or greater migraine-related disability.",
        "Citation pending — Symptoms beyond head pain.",
        "Citation pending — Migraine recognition before diagnosis.",
        AHS_STUDY,
        "Citation pending — CGRP monoclonal antibody response rates and study population.",
    ]
    return f'''<main id="main">
<section class="ja-hero" aria-labelledby="ja-hero-title">
  {face_grid()}
  <div class="ja-hero__veil" aria-hidden="true"></div>
  <div class="ja-container ja-hero__content">
    <h1 id="ja-hero-title">
      <span class="ja-hero__lead ja-hero-lead-in">More than</span>
      <span class="ja-hero__number ja-hero-highlight">40 million</span>
      <span class="ja-hero__line ja-hero-continuation">Americans live with migraine{sup(1)}</span>
    </h1>
    <p class="ja-hero__subtitle ja-hero-subtitle">Fewer than <strong>1 in 3</strong> have sought care, been diagnosed, and are taking recommended acute medication.{sup(2)}</p>
    <span class="ja-hero__rule" aria-hidden="true"></span>
    <p class="ja-hero__led"><span class="ja-small" style="font-style:italic;font-weight:500">Led by:</span><img src="/assets/img/logos/ahs-horizontal-2-color.svg" alt="American Headache Society" width="121" height="48"></p>
  </div>
  <button class="ja-hero__pause" type="button" aria-pressed="false"><svg class="ja-pausei" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 1h3v10H2zM7 1h3v10H7z"/></svg><svg class="ja-play" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 1l9 5-9 5z"/></svg><span class="ja-pause-label">Pause animation</span></button>
</section>
<section class="ja-section ja-intro" aria-labelledby="ja-intro-title">
  <div class="ja-container ja-intro__grid">
    <div class="ja-intro__media ja-fpo"><img src="{PHOTO}" alt="A clinician listens to a patient during a consultation." width="1871" height="840" loading="lazy"><span class="ja-fpo__label" aria-hidden="true">FPO</span></div>
    <div class="ja-intro__text">
      <span class="ja-rule" aria-hidden="true"></span>
      <h2 class="ja-h2" id="ja-intro-title">Better migraine care starts with <span class="ja-hl">asking</span></h2>
      <div class="ja-prose ja-body"><p>Migraine is diagnosable and treatable, yet the World Health Organization ranks it a leading cause of disability worldwide.{sup(3)} Asking about how headaches affect daily life can help identify patients who may benefit from diagnosis and effective treatment.</p></div>
      {link("See the Question", URL["ask"])}
    </div>
  </div>
</section>
<section class="ja-section ja-question" aria-labelledby="ja-question-title">
  <div class="ja-container ja-question__grid">
    <div class="ja-question__intro">
      <p class="ja-eyebrow ja-label">Just Ask</p>
      <h2 class="ja-h2" id="ja-question-title">One question that fits into every visit</h2>
    </div>
    <figure class="ja-question__panel">
      <blockquote class="ja-question__bracket ja-statement">“{Q_HL}”</blockquote>
    </figure>
    <div class="ja-question__after">
      <div class="ja-prose ja-body"><p>Patients may keep working, caring for family, and going to school despite disabling symptoms. This brief question focuses on what headaches interfere with and can be added to intake, rooming, or a routine visit.</p></div>
      {link("Simple by Design", URL["ask"])}
    </div>
  </div>
</section>
<section class="ja-section ja-stats" aria-labelledby="ja-stats-title">
  <span class="ja-pattern" aria-hidden="true"></span>
  <div class="ja-container">
    <span class="ja-rule" aria-hidden="true"></span>
    <h2 class="ja-h2" id="ja-stats-title">A disability that can hide in plain sight</h2>
    <div class="ja-prose ja-body ja-stats__intro"><p>Migraine is a neurological disease that can affect work, family, and everyday activities. Some patients assume their symptoms are simply part of life or do not realize effective treatment is available.</p></div>
    <ul class="ja-stats__grid">{stats}</ul>
  </div>
</section>
{quote_band("I was waiting for them to tell me, and they were waiting for me to ask.", "Clinician, AHS Study", 10)}
<section class="ja-section ja-treatment" aria-labelledby="ja-treat-title">
  <div class="ja-container ja-treatment__grid">
    <div class="ja-treatment__text">
      <h2 class="ja-h2" id="ja-treat-title">More ways to treat migraine</h2>
      <div class="ja-prose ja-body"><p>Migraine treatment has advanced significantly in recent years, with new options for acute and preventive care. Identifying patients with migraine is the first step toward finding a treatment plan that fits their needs.</p></div>
      {link("After the Yes: Guidance and Resources", URL["aty"])}
    </div>
    <figure class="ja-evidence">
      <span class="ja-evidence__value ja-display">57–64%</span>
      <figcaption class="ja-evidence__text ja-evidence-qualifier">of patients on CGRP monoclonal antibodies cut their monthly migraine days in half or more.{sup(11)}</figcaption>
    </figure>
  </div>
</section>
<section class="ja-section ja-partners" aria-labelledby="ja-partners-title">
  <div class="ja-container">
    <div class="ja-partners__head">
      <div><h2 class="ja-h2" id="ja-partners-title">Developed with clinicians who see patients every day</h2></div>
      <div>
        <div class="ja-prose ja-body"><p>The American Headache Society developed Just Ask using research with more than 130 frontline and specialist clinicians, with support from partner organizations across primary care.{sup(10)}</p></div>
        {link("Why Ask About Migraine", URL["why"])}
      </div>
    </div>
    {partners_logos()}
  </div>
</section>
{cta_band("One question,", "asked of every patient, can bring migraine into the open", buttons=button("Just Ask", URL["ask"]), id_="ja-cta-title")}
{references(refs)}
</main>'''


# =====================================================================================
# 1.0 WHY ASK
# =====================================================================================
def why_ask():
    logos = '<li class="ja-partner"><img src="/assets/img/logos/ahs-horizontal-2-color.svg" alt="American Headache Society" width="121" height="48"></li>' + \
        "".join(f'<li class="ja-partner"><span class="ja-partner__placeholder ja-small">Logo {i}</span></li>' for i in range(1, 7))
    return f'''<main id="main" class="ja-interior">
{page_hero("Why Ask", "The case for asking", "Migraine affects daily life for millions of people, but many never receive a diagnosis or treatment. A routine question about headache-related interference gives clinicians a practical way to identify patients who may need further evaluation.", variant="media", media=hero_photo())}
<section class="ja-section ja-partners ja-partners--strip" aria-label="AHS and partner organizations"><div class="ja-container">
  <ul class="ja-partners__logos" aria-label="AHS and partner organizations">{logos}</ul>
</div></section>
<section class="ja-section ja-stats" aria-labelledby="mv-common">
  <span class="ja-pattern" aria-hidden="true"></span>
  <div class="ja-container">
    {rule_h2("A common disease with a significant impact", "mv-common")}
    <div class="ja-prose ja-body ja-stats__intro"><p>Migraine is a neurological disease that can involve sensory, vestibular, cognitive, and gastrointestinal symptoms, sometimes without severe headache. It affects people across demographics and often disrupts work, school, and family life.{sup(1)}</p></div>
    <ul class="ja-stats__grid">{stat("1 in 6", f"U.S. adults live with migraine or severe headache.{sup(2)}")}{stat("2×", f"About twice as common in women.{sup(3)}")}{stat("113M", f"workdays lost to migraine each year in the U.S.{sup(4)}")}{stat("42%", f"live with moderate or greater migraine-related disability.{sup(5)}")}</ul>
  </div>
</section>
<section class="ja-section ja-section--tint ja-text-section ja-text-section--aside">
  <div class="ja-container"><div class="ja-text-section__grid"><div>
    {rule_h2("The diagnosis gap")}
    <p class="ja-body ja-text-section__body">Patients with migraine may see a clinician for other concerns without ever discussing their headaches. When symptoms go unmentioned, opportunities for diagnosis and effective treatment are missed.{sup(6)}</p>
    <ol class="ja-bars">
      <li class="ja-bar"><div class="ja-bar__head"><span class="ja-body ja-bar__label">Currently consulting a clinician{sup(7)}</span><span class="ja-bar__value">38.7%</span></div><div class="ja-bar__track" aria-hidden="true"><span class="ja-bar__fill" style="width: 38.7%"></span></div></li>
      <li class="ja-bar"><div class="ja-bar__head"><span class="ja-body ja-bar__label">Consulting and accurately diagnosed{sup(7)}</span><span class="ja-bar__value">27.0%</span></div><div class="ja-bar__track" aria-hidden="true"><span class="ja-bar__fill" style="width: 27.0%"></span></div></li>
      <li class="ja-bar"><div class="ja-bar__head"><span class="ja-body ja-bar__label">Consulting, diagnosed, and on appropriate treatment{sup(7)}</span><span class="ja-bar__value">14.4%</span></div><div class="ja-bar__track" aria-hidden="true"><span class="ja-bar__fill" style="width: 14.4%"></span></div></li>
    </ol>
  </div>
  <aside class="ja-text-section__aside">{callout("Wider for some patients", f"Diagnosis rates fall further for Black and Hispanic patients compared with white patients, and for men compared with women.{sup(8)}")}</aside>
  </div></div>
</section>
<section class="ja-section ja-stats" aria-labelledby="mv-clin">
  <div class="ja-container">
    {rule_h2("What frontline clinicians told us", "mv-clin")}
    <div class="ja-prose ja-body ja-stats__intro"><p>AHS surveyed and interviewed clinicians across primary care, women’s health, urgent care, and specialty settings to understand what gets in the way of migraine diagnosis and which tools would help in everyday practice.{sup(9)}</p></div>
    <ul class="ja-stats__grid">{stat("133", f"clinicians screened.{sup(9)}")}{stat("17", f"in-depth interviews.{sup(9)}")}{stat("8", f"specialties represented.{sup(9)}")}</ul>
    <div class="ja-findings">
      <div class="ja-finding"><div class="ja-finding__copy"><h3 class="ja-h3">Clinicians want practical support</h3><p class="ja-body ja-finding__text">Clinicians reported confidence in managing migraine, especially with more experience diagnosing it. They also asked for concise tools, actionable guidance, and a clear path after screening.{sup(9)}</p></div>{pullquote("If the scaffolding did some of the holding, I wouldn’t have to be heroic.", "Family Medicine, AHS Study", 9, "finding")}</div>
      <div class="ja-finding"><div class="ja-finding__copy"><h3 class="ja-h3">Patients often do not bring up headaches</h3><p class="ja-body ja-finding__text">Patients may attribute recurring symptoms to stress, sinus problems, or hormones, or dismiss them as “just a headache.” A routine question helps identify symptoms they might otherwise leave out.{sup(9)}</p></div>{pullquote("They present as under-dramatic a lot of the time.", "Family Medicine, AHS Study", 9, "finding")}</div>
    </div>
  </div>
</section>
<section class="ja-section ja-question ja-question--top" aria-labelledby="mv-q">
  <div class="ja-container ja-question__grid">
    <div class="ja-question__intro">{rule_h2("One question that fits into routine care", "mv-q")}</div>
    <div class="ja-question__side"><figure class="ja-question__panel"><blockquote class="ja-question__bracket ja-statement">“{Q_HL}”</blockquote></figure><div class="ja-stat ja-stat--wide"><span class="ja-stat__value ja-statistic">94%</span><span class="ja-stat__rule" aria-hidden="true"></span><p class="ja-stat__label ja-body">of patients with episodic disabling headache in primary care had migraine.{sup(11)}</p></div></div>
    <div class="ja-question__after">
      <div class="ja-prose ja-body"><p>A consistent screening question creates an opportunity to recognize headache-related disability, even when migraine is not the reason for the visit.{sup(10)}</p></div>
      {button("Why This Question?", URL["ask"])}
    </div>
  </div>
</section>
{quote_band("Good migraine care shouldn’t depend on which clinician, or even what mood that clinician is in.", "Family Medicine, AHS Study", 9)}
<section class="ja-section ja-stats" aria-labelledby="mv-support">
  <div class="ja-container">
    {rule_h2("Practical guidance for after the yes", "mv-support")}
    <div class="ja-prose ja-body ja-stats__intro"><p>Many patients can begin migraine evaluation and treatment in frontline care. AHS offers concise guidance for diagnosis, acute and preventive treatment, follow-up, and referral.{sup(12)}</p></div>
    <ul class="ja-stats__grid">{stat("9", f"migraine-specific medications approved by the FDA since 2018.{sup(13)}")}{stat("57.5–63.6%", f"of real-world patients with chronic migraine cut monthly migraine days in half or more on CGRP antibodies.{sup(14)}")}</ul>
    <div class="ja-stats__link">{button("After the Yes: Guidance and Resources", URL["aty"])}</div>
  </div>
</section>
{cta_band("Make the question", "part of your routine", body="One question can help more patients with migraine get the diagnosis and care they need.", buttons=button("Just Ask", URL["ask"]), id_="mv-cta")}
{references(["Citation pending.", "Citation pending.", "Citation pending.", "Citation pending.", "Citation pending.", "Citation pending.", OVERCOME, "Citation pending.", AHS_STUDY, "Citation pending.", "Citation pending.", "Citation pending.", "Citation pending.", "Citation pending."])}
</main>'''


# =====================================================================================
# 2.0 THE ASK
# =====================================================================================
def the_ask():
    cards1 = "".join([
        info_card("Quick to ask", "A single question can fit into existing intake forms, rooming, or clinical visits. It takes just seconds to ask and can be documented alongside other routine screening questions, making migraine screening easier to incorporate into everyday care."),
        info_card("Focus on function", f"Patients may normalize symptoms or manage them quietly with OTC medication. Asking about daily life reveals what’s at stake.{sup(3)}", inner=pullquote("Pain scores aren’t usually very useful with my patients.", "Family Medicine, AHS Study", 3)),
        info_card("Ask what interfered, not what was missed", f"Patients who show up to work or school through symptoms would answer no to “missed” but yes to “interfered.”{sup(3)}", inner=pullquote("A lot of my patients can’t miss work. They’re going to work and throwing up.", "OB/GYN, AHS Study", 3)),
        info_card("Make headache part of routine care", "Asking about headaches helps patients recognize migraine as a legitimate health concern, especially when they’ve spent years dismissing or normalizing their symptoms. That recognition can extend beyond the exam room. Sharing what they’ve learned may help friends and family recognize their own symptoms and seek care. One question can have an impact well beyond the patient being asked."),
    ])
    cards2 = "".join([
        info_card("On the intake form", "Patients answer on a paper or digital intake form before the visit, so a “yes” arrives with the rest of their history."),
        info_card("During rooming", "A nurse or medical assistant asks alongside vitals and other routine questions, then flags a “yes” for the clinician."),
        info_card("In the exam room", "The clinician asks while reviewing symptoms or the reason for the visit and can follow up on a “yes” during the same visit or at a dedicated follow-up."),
        info_card("As an EHR prompt", "A prompt or template in the EHR reminds staff or the clinician to ask, helping make screening a consistent part of routine care."),
    ])
    hero_panel = f'''<div class="ja-qpanel"><p class="ja-question ja-qpanel__quote">“{Q_HL}”</p><div class="ja-qpanel__actions">{copy_button("ja-button ja-button--outline")}</div></div>'''
    return f'''<main id="main" class="ja-interior">
{page_hero("The Ask", "One question to help identify patients with migraine", f"Developed with input from frontline clinicians, this question is designed to fit into routine visits and uncover headaches that interfere with daily life.{sup(1)}", variant="question", media=hero_panel)}
<section class="ja-section ja-card-grid">
  <div class="ja-container">
    {rule_h2("Why this question?")}
    <p class="ja-body ja-card-grid__intro">Many people with migraine do not receive a diagnosis and recommended treatment. Asking every patient about headache-related interference can reveal symptoms they might not otherwise mention.{sup(2)}</p>
    <ul class="ja-card-grid__list">{cards1}</ul>
    <div class="ja-card-grid__after">{button("See the Case for Asking", URL["why"])}</div>
  </div>
</section>
<section class="ja-section ja-section--tint ja-card-grid ja-card-grid--4">
  <div class="ja-container">
    {rule_h2("Make it part of your existing workflow")}
    <p class="ja-body ja-card-grid__intro">Asking every patient matters more than who asks or when. The Ask is most effective when it’s built into the existing workflow, tied to a clear next step, and tested with your team before rollout.</p>
    <ul class="ja-card-grid__list">{cards2}</ul>
  </div>
</section>
<section class="ja-section ja-text-section ja-text-section--aside">
  <div class="ja-container"><div class="ja-text-section__grid"><div>
    {rule_h2("When the answer is yes")}
    <p class="ja-body ja-text-section__body">A “yes” does not establish a migraine diagnosis. It identifies a patient who may benefit from further questions, assessment for red flags, and a plan for diagnosis and treatment.{sup(4)}</p>
    <div class="ja-text-section__more">{button("After the Yes: Guidance and Resources", URL["aty"])}</div>
  </div>
  <aside class="ja-text-section__aside">{callout("Even with two minutes left", "When a “yes” appears late in the visit, identifying the likely diagnosis and scheduling a follow-up still moves care forward.", extra=pullquote("I’d rather say, ‘I think it’s this. Let’s see how that goes.’", "OB/GYN, AHS Study", 3, style="margin-top: 24px"))}</aside>
  </div></div>
</section>
{cta_band("Share it", "with your team", body="Share the question with staff who manage intake, rooming, and documentation so patients receive a consistent screening experience.", buttons=copy_button(), share=False, question=True, id_="ask-cta")}
{references(["Citation pending.", OVERCOME, AHS_STUDY, "Citation pending."])}
</main>'''


# =====================================================================================
# 3.0 AFTER THE YES
# =====================================================================================
def step_card(n, time, title, href, text, go):
    return (f'<li><article class="ja-step-card"><div class="ja-step-card__head"><span class="ja-step-card__circle" aria-hidden="true">{n}</span><span class="ja-label ja-step-card__time">{time}</span></div>'
            f'<h3 class="ja-h3 ja-step-card__title"><a href="{href}"><span class="ja-visually-hidden">Step {n}: </span>{title}</a></h3>'
            f'<p class="ja-body ja-step-card__text">{text}</p>'
            f'<span class="ja-step-card__go" aria-hidden="true"><span class="ja-step-card__go-text">{go[0]} <span class="ja-nowrap">{go[1]} {ARROW}</span></span></span></article></li>')


def after_the_yes():
    gl = lambda g: reslinks(("See Guidance and Resources", f'{URL["library"]}?group={g}'))  # noqa: E731
    return f'''<main id="main" class="ja-interior">
{page_hero("After the Yes", "What to do after a patient says yes", "A “yes” opens the path to diagnosis. Migraine can often be effectively treated and managed in frontline practice. These practical resources guide you through evaluation, treatment, and follow-up.", variant="media", media=hero_photo())}
<section class="ja-section ja-text-section ja-text-section--aside">
  <div class="ja-container">
    <div class="ja-text-section__grid"><div>
      {rule_h2("Three steps after the yes")}
      <p class="ja-body ja-text-section__body">Start with the step your patient needs today. Assessment, treatment planning, and follow-up can take place across visits when clinically appropriate.</p>
    </div>
    <aside class="ja-text-section__aside">{callout("Only have two minutes?", "Share a preliminary assessment, let your patient know treatment options are available, and arrange a follow-up for further evaluation.")}</aside>
    </div>
    <ol class="ja-step-cards">
      {step_card(1, "Five minutes", "Diagnosing migraine", URL["diag"], "Discuss acute treatment options and help the patient leave with a clear plan.", ("Diagnosing", "Migraine"))}
      {step_card(2, "Ten minutes", "Treating migraine", URL["treat"], "Review response, consider prevention when appropriate, and determine whether specialist input is needed.", ("Treating", "Migraine"))}
      {step_card(3, "At follow-up", "Ongoing care", URL["ongoing"], "Check how treatment is working, adjust or add prevention, and know when to bring in a specialist.", ("Ongoing", "Care"))}
    </ol>
    <div style="margin-top: 48px">
      <aside class="ja-featured" aria-labelledby="aty-feat"><span class="ja-pattern ja-featured__pattern" aria-hidden="true"></span>
        <div><span class="ja-tag ja-tag--format ja-tag--tool ja-featured__tag">Tool</span><h3 class="ja-h3" id="aty-feat">Migraine Management Flowchart</h3><p class="ja-body ja-featured__text">Go from ID Migraine screening and red flags through ED or outpatient workup, acute and preventive treatment, and when to consult neurology.</p><div class="ja-featured__actions">{button("Open the Flowchart", "https://americanheadachesociety.org/resources/primary-care/migraine-flowchart")}</div></div>
        <div class="ja-featured__preview ja-fpo"><img src="{PHOTO}" alt="" width="1871" height="840" loading="lazy"><span class="ja-fpo__label" aria-hidden="true">FPO</span></div>
      </aside>
    </div>
  </div>
</section>
<section class="ja-section ja-section--tint ja-card-grid ja-card-grid--3">
  <div class="ja-container">
    {rule_h2("Guidance for different patient needs")}
    <p class="ja-body ja-card-grid__intro">Migraine presents differently across populations and over a lifetime, and treatment shifts with it. We recommend annual screening from adolescence through menopause to track changes.{sup(1)}</p>
    <ul class="ja-card-grid__list">
      {info_card("Hormones, contraception, and pregnancy", "Navigate menstrual migraine, aura and estrogen use, and care through pregnancy, postpartum, and menopause.", gl("women"))}
      {info_card("Children and teens", "See how migraine presents in younger patients, treatment options, and school support resources.", gl("peds"))}
      {info_card("Older adults", "Evaluate new headache after 50 and choose treatment that fits alongside other medications and comorbidities.", gl("older"))}
    </ul>
  </div>
</section>
<section class="ja-section ja-text-section">
  <div class="ja-container">
    {rule_h2("Build your migraine expertise")}
    <p class="ja-body ja-text-section__body">Explore free clinical education and practical resources designed for clinicians who diagnose and treat migraine in everyday practice.</p>
    <ul class="ja-card-grid__list ja-text-section__cards">
      <li>{resource("Podcast", "Headache and Primary Care", "Explore practical approaches to diagnosing, treating, and managing headache disorders in primary care, with insights you can apply to everyday patient care.", "https://podcasters.spotify.com/pod/show/primarycare/episodes/What-Primary-Care-Providers-Should-Know-About-Newer-Migraine-Medications-e23v4jl/a-a9qssfl")}</li>
      <li>{resource("Video", "Headache and Primary Care", "Build your knowledge on evaluating and managing headache disorders with expert-led guidance designed for frontline clinicians.", "https://americanheadachesociety.org/resources/primary-care/videos", action="Watch Videos")}</li>
    </ul>
    <div class="ja-text-section__more">{button("Browse All Resources", URL["library"])}</div>
  </div>
</section>
{cta_band("Start", "with one question", body="One question can help identify patients with migraine who might otherwise go undiagnosed. Make it part of your routine care.", buttons=button("Just Ask", URL["ask"]), id_="aty-cta")}
{references(["Citation pending."])}
</main>'''


# =====================================================================================
# 3.1 DIAGNOSING
# =====================================================================================
def specific_cards(cards, cols=3):
    return f'''<section class="ja-section ja-card-grid ja-card-grid--{cols}">
  <div class="ja-container">
    {rule_h2("What changes for specific patients")}
    <ul class="ja-card-grid__list">{cards}</ul>
  </div>
</section>'''


ATY = ("After the Yes", URL["aty"])


def diagnosing():
    return f'''<main id="main" class="ja-interior">
{page_hero("After the Yes · Step 1", "How to evaluate a patient for migraine", f"For many patients, a focused history and neurological examination can support a clinical migraine diagnosis. Screen for red flags and consider other causes before confirming the diagnosis.{sup(1)}", variant="step", eyebrow_href=ATY)}
{step_nav(1)}
<section class="ja-section ja-text-section">
  <div class="ja-container">
    {rule_h2("Start with three migraine screening questions")}
    <p class="ja-body ja-text-section__body">Two or three yes answers on the ID Migraine screen signal a 93% likelihood of migraine. The screen doesn’t rule out secondary headache.</p>
    <div class="ja-list-panel"><ol class="ja-list ja-list--numbered"><li class="ja-body">Does light bother you when you have a headache?</li><li class="ja-body">Have headaches limited your activities for a day or more in the last three months?</li><li class="ja-body">Are you nauseated or sick to your stomach when you have a headache?</li></ol></div>
    <ul class="ja-card-grid__list">
      {info_card("Migraine without aura", f"Symptoms last 4 to 72 hours, often affect one side of the head, and have a pulsing quality. Routine activity makes them worse, accompanied by nausea or light and sound sensitivity.{sup(2)}")}
      {info_card("Migraine with aura", f"Reversible neurological symptoms, most often visual, that build over 5 to 20 minutes and resolve within an hour. Many patients with aura also have migraine without it.{sup(3)}")}
    </ul>
    <div class="ja-text-section__more" style="max-width: none">{reslinks(("How to Diagnose Migraine", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/AHS-First-Contact-HowToDiagnose_Migraine.pdf", "Quick Guide · PDF", "quick-guide"))}</div>
  </div>
</section>
<section class="ja-section ja-section--tint ja-text-section ja-text-section--split">
  <div class="ja-container"><div class="ja-text-section__split">
    <div>{rule_h2("Review prescription and OTC medication use")}</div>
    <div class="ja-text-section__lead"><p class="ja-text-section__lede">Ask about OTC and combination products by name and how often your patient takes them. Many patients don’t count these as medication, and frequent use can lead to medication overuse headache.{sup(4)}</p><div class="ja-text-section__more">{button("Medication Overuse Limits", URL["treat"] + "#treat-early")}</div></div>
  </div></div>
</section>
<section class="ja-section ja-card-grid ja-card-grid--2">
  <div class="ja-container">
    {rule_h2("Identify red flags")}
    <p class="ja-body ja-card-grid__intro">While most patients won’t have any, red flags fall into two groups, and each calls for a different response.{sup(5)}</p>
    <ul class="ja-card-grid__list">
      {info_card("Needs urgent evaluation", "", inverse=True, inner='<ul class="ja-list ja-list--bullet"><li class="ja-body">Patient experiencing fever</li><li class="ja-body">New neurological deficit</li><li class="ja-body">Thunderclap onset reaching peak intensity within a minute</li><li class="ja-body">Onset during sexual activity</li></ul>')}
      {info_card("Consider imaging or more tests", "", inner='<ul class="ja-list ja-list--bullet"><li class="ja-body">Patient experiencing new or worsening headache</li><li class="ja-body">Significant change in pattern</li><li class="ja-body">New onset after 50</li><li class="ja-body">Signs of systemic illness, predisposing conditions including pregnancy</li><li class="ja-body">Headache that worsens when standing, starts with coughing or exertion, or wakes the patient from sleep</li><li class="ja-body">Pain always on the same side</li><li class="ja-body">No response to treatment</li></ul>')}
    </ul>
    <div class="ja-card-grid__after ja-card-grid__pair">
      {callout("What isn’t a red flag", f"Mid-face pain that patients interpret as sinus trouble and pain at the base of the skull are common migraine symptoms. A stable pattern with a normal neurological exam rarely needs imaging.{sup(6)}")}
      {resource("Quick Guide", "When Does a Patient With Headache Need a Workup?", "Know which symptoms call for urgent evaluation, imaging, or more tests.", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/AHS-First-Contact-Headache-WorkUp.pdf")}
    </div>
  </div>
</section>
<section class="ja-section ja-section--tint ja-text-section ja-text-section--split">
  <div class="ja-container"><div class="ja-text-section__split">
    <div>{rule_h2("Explain the diagnosis and next steps")}</div>
    <div class="ja-text-section__lead"><p class="ja-text-section__lede">Name migraine as a neurological disease with effective treatment, and take your patient’s experience seriously. If they’ve heard sinus or stress before, update that explanation without discrediting earlier care.</p></div>
  </div></div>
</section>
{specific_cards("".join([
    info_card("Hormones, contraception, and pregnancy", f"Note whether symptoms follow the menstrual cycle and ask about aura, which shapes contraception choices. We recommend yearly migraine screening from adolescence through menopause.{sup(7)}", reslinks(("Routine Migraine Screening in Women’s Health", "https://headachejournal.onlinelibrary.wiley.com/doi/10.1111/head.70023"))),
    info_card("Children and teens", f"Migraine in children often runs shorter and affects both sides of the head. A focused history and exam help you tell primary from secondary headache.{sup(8)}", reslinks(("Diagnosing and Treating Pediatric Migraine", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/Diagnosing-and-Treating-Pediatric-Migraine.pdf"))),
    info_card("Older adults", f"New headache after 50 calls for evaluation of other causes, including giant cell arteritis, before you confirm migraine.{sup(9)}", reslinks(("Headache in Older Adults", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/AHS-First-Contact-Headache-Older-Adults.pdf"))),
]))}
{page_nav((URL["aty"], "Back", "After the Yes"), (URL["treat"], "Next: Step 2", "Treating Migraine"))}
{references(pending(9))}
</main>'''


# =====================================================================================
# 3.2 TREATING
# =====================================================================================
def treating():
    return f'''<main id="main" class="ja-interior">
{page_hero("After the Yes · Step 2", "Treating migraine with acute and preventive care", "Every patient diagnosed with migraine needs an acute plan, and some may benefit from prevention. Treatment options have expanded in recent years, and you can start most of them in frontline care.", variant="step", eyebrow_href=ATY)}
{step_nav(2)}
<section class="ja-section ja-section--tint ja-text-section ja-text-section--split">
  <div class="ja-container"><div class="ja-text-section__split">
    <div>{rule_h2("Agree on treatment goals")}</div>
    <div class="ja-text-section__lead"><p class="ja-text-section__lede">Talk through what treatment can realistically do and how long it takes to work. Ask your patient to track migraine days and what they disrupt, and discuss common triggers without placing blame.</p></div>
  </div></div>
</section>
<section class="ja-section ja-card-grid ja-card-grid--2">
  <div class="ja-container">
    {rule_h2("Choose acute treatment based on patient needs")}
    <p class="ja-body ja-card-grid__intro">Aim for relief within two hours, a return to daily activities, and little need for rescue medication.{sup(1)}</p>
    <ul class="ja-card-grid__list">
      {info_card("Mild symptoms", f"If your patient can keep up with their routine, start with common analgesics and NSAIDs.{sup(2)}")}
      {info_card("Moderate to severe symptoms", f"If symptoms disrupt the routine, use triptans, gepants, ditans, or DHE, alone or with an NSAID or antiemetic. Choose a non-oral route for vomiting or fast-peaking symptoms.{sup(2)}")}
    </ul>
    <div class="ja-card-grid__after ja-card-grid__pair" id="treat-early">
      {callout("Treat early, within limits", f"Encourage early use and set limits: 14 days a month for simple analgesics and nine for other acute medications to prevent medication overuse headache.{sup(3)}")}
      {resource("Quick Guide", "Choosing the Right Acute Treatment", "Match acute medication and route to symptom severity and your patient’s needs.", "https://d1fakw34cbtrm5.cloudfront.net/6.3-Primary-Care/AHS-First-Contact-Writeup-Acute-Treatment-new-v9.pdf")}
    </div>
  </div>
</section>
<section class="ja-section ja-section--tint ja-text-section ja-text-section--aside">
  <div class="ja-container">
    {rule_h2("Know when to consider prevention")}
    <p class="ja-body ja-text-section__body">Offer prevention based on how often symptoms occur and how much they disrupt daily life. We consider CGRP-targeting therapies a first-line option.{sup(4)}</p>
    <div class="ja-text-section__grid ja-text-section__grid--sub">
      <div class="ja-text-section__sub"><h3 class="ja-h3">Choosing a preventive treatment</h3><p class="ja-body">Pick an option that also treats a comorbidity when possible, and weigh the side effects that matter most to your patient, such as weight change or sleepiness.{sup(5)}</p></div>
      <aside class="ja-text-section__aside">{callout("Give it time", f"Prevention succeeds when migraine days drop by half or more after a three- to six-month trial at the target dose.{sup(6)}")}</aside>
    </div>
    <ul class="ja-card-grid__list ja-text-section__cards">
      <li>{resource("Quick Guide", "Choosing the Right Preventive Treatment", "Select a preventive treatment based on comorbidities, side effects, and preferences.", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/AHS-First-Contact-PreventativeTreatment.pdf")}</li>
      <li>{resource("Guideline", "CGRP-Targeting Therapies as a First-Line Option", "Our position on CGRP-targeting therapies as a first-line preventive option.", "https://headachejournal.onlinelibrary.wiley.com/doi/full/10.1111/head.14692")}</li>
    </ul>
  </div>
</section>
<section class="ja-section ja-text-section ja-text-section--split" id="getting-covered">
  <div class="ja-container"><div class="ja-text-section__split">
    <div>{rule_h2("Help patients access prescribed treatment")}</div>
    <div class="ja-text-section__lead"><p class="ja-text-section__lede">Prior authorization, step therapy, and quantity limits can delay care. Documenting migraine days and past treatments makes approval easier.{sup(7)}</p><div class="ja-text-section__more">{reslinks(("Prior Authorization Letter Templates", "https://americanheadachesociety.org/resources/clinicians/clinical-practice-resources/downloadable-prior-authorization-letter-templates", "Tool", "tool"))}</div></div>
  </div></div>
</section>
{specific_cards("".join([
    info_card("Hormones, contraception, and pregnancy", f"Weigh stroke risk before prescribing estrogen-containing contraception to patients with aura, and consider options for menstrual migraine. Know which treatments to use or avoid in pregnancy and breastfeeding, and when to refer.{sup(8)}", reslinks(("Contraceptive Options for Women With Migraine", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/AHS-First-Contact-Contraceptive-Options.pdf", "Quick Guide", "quick-guide"))),
    info_card("Children and teens", f"Choose first-line acute options for children, learn which migraine-specific treatments are approved for adolescents, and lead prevention with behavioral approaches.{sup(9)}", reslinks(("Pediatric Migraine Treatment Options and Further Evaluation", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/AHS-First-Contact-Pediatric-treatment.pdf", "Quick Guide", "quick-guide"))),
    info_card("Older adults", f"Consider cardiovascular risk and current medications when you choose acute and preventive treatment.{sup(10)}"),
]))}
{page_nav((URL["diag"], "Back: Step 1", "Diagnosing Migraine"), (URL["ongoing"], "Next: Step 3", "Ongoing Care"))}
{references(pending(10))}
</main>'''


# =====================================================================================
# 3.3 ONGOING CARE
# =====================================================================================
def ongoing():
    quote = pullquote("We’re just inconsistent about closing the loop.", "Internal Medicine, AHS Study", 1, style="margin-top: 32px; max-width: 720px")
    return f'''<main id="main" class="ja-interior">
{page_hero("After the Yes · Step 3", "Ongoing migraine care and management", "A clear follow-up plan helps you assess treatment response, address access barriers, and adjust care. Schedule the next check-in before the patient leaves when possible.", variant="step", extra=quote, eyebrow_href=ATY)}
{step_nav(3)}
<section class="ja-section ja-section--tint ja-text-section">
  <div class="ja-container">
    {rule_h2("Plan the next check-in")}
    <ol class="ja-timeline">
      <li><h3 class="ja-h3">After a new acute treatment</h3><p class="ja-body ja-timeline__text">Once your patient has used medication three or four times.</p></li>
      <li><h3 class="ja-h3">After starting prevention</h3><p class="ja-body ja-timeline__text">Reassess three to six months in, at the target dosage.{sup(2)}</p></li>
      <li><h3 class="ja-h3">Once goals are met</h3><p class="ja-body ja-timeline__text">Every 6 to 12 months.{sup(2)}</p></li>
    </ol>
    <p class="ja-body ja-timeline-note">Catch treatment failure early with a quick phone call, portal message or nurse check-in.</p>
  </div>
</section>
<section class="ja-section ja-text-section">
  <div class="ja-container">
    {rule_h2("What to assess at follow-up")}
    <div class="ja-list-panel"><ul class="ja-list ja-list--check">
      <li class="ja-body">Number of migraine days and how much they disrupt daily life</li>
      <li class="ja-body">How well and how fast acute treatment works</li>
      <li class="ja-body">How often your patient uses acute and OTC medications</li>
      <li class="ja-body">Whether your patient could fill, afford, and take treatment as planned</li>
    </ul></div>
  </div>
</section>
<section class="ja-section ja-text-section">
  <div class="ja-container">
    {rule_h2("If symptoms are not improving")}
    <p class="ja-body ja-text-section__body">Check access first. A treatment your patient couldn’t fill, afford, or take early can look like a failure, and quantity limits can lead patients to ration doses.{sup(3)}</p>
    <h3 class="ja-label" style="margin-top: 32px">Common reasons</h3>
    <ul class="ja-list ja-list--bullet ja-list--cols" style="margin-top: 12px">
      <li class="ja-body">Medication overuse</li><li class="ja-body">Taken too late</li><li class="ja-body">Dose too low or trial too short</li><li class="ja-body">Poor match between route and symptom</li><li class="ja-body">No antiemetic</li><li class="ja-body">Uncertain diagnosis</li>
    </ul>
    <div class="ja-text-section__more">{button("Getting Treatment Covered", URL["treat"] + "#getting-covered")}</div>
  </div>
</section>
<section class="ja-section ja-section--tint ja-text-section ja-text-section--split">
  <div class="ja-container"><div class="ja-text-section__split">
    <div>{rule_h2("When treatment goals are met")}</div>
    <div class="ja-text-section__lead"><p class="ja-text-section__lede">Continue preventive treatment for one to two years, then discuss tapering or discontinuing. However, some patients choose to continue longer.{sup(4)}</p><div class="ja-text-section__more">{reslinks(("Counseling Patients on Preventive Treatment", "https://www.youtube.com/watch?v=jid0IkoXG5c", "Video", "video"))}</div></div>
  </div></div>
</section>
<section class="ja-section ja-text-section ja-text-section--aside">
  <div class="ja-container"><div class="ja-text-section__grid"><div>
    {rule_h2("When to involve a specialist")}
    <p class="ja-body ja-text-section__body">Migraine can often be effectively managed in frontline care. When specialist input is needed, you can continue providing care while coordinating a referral or consultation.{sup(5)}</p>
    <ul class="ja-list ja-list--bullet" style="margin-top: 24px; max-width: 720px">
      <li class="ja-body">Red flags that need urgent evaluation</li><li class="ja-body">Pregnancy or breastfeeding</li><li class="ja-body">Migraine-specific acute treatment still isn’t working after adjustment</li><li class="ja-body">Prevention goals remain unmet after adjustment</li>
    </ul>
    {resource("Tool", "Find a Headache Specialist", "Search the American Migraine Foundation directory for a headache specialist near your patient.", "https://americanmigrainefoundation.org/find-a-doctor/", style="margin-top: 32px; max-width: 720px")}
  </div>
  <aside class="ja-text-section__aside">{callout("Consider an e-consult", "A specialist can review the history and plan without a visit, so you continue care in the meantime.", extra=pullquote("E-consult or a secure message: here is the history, here is what I have tried, am I missing anything?", "Family Medicine NP, AHS Study", 1, style="margin-top: 24px"))}</aside>
  </div></div>
</section>
{specific_cards("".join([
    info_card("Hormones, contraception, and pregnancy", f"Revisit the plan when your patient is planning pregnancy, is postpartum, or enters perimenopause, since migraine often changes during these stages.{sup(6)}"),
    info_card("Children and teens", "Give families and schools a written action plan, and support school accommodations when migraine affects attendance.", reslinks(("Pediatric Migraine Action Plan (PedMAP)", "https://d1fakw34cbtrm5.cloudfront.net/PDFs/Migraine-Quick-Guides/Headache-2018-Peretz-Migraine-Action-Plan-MAP.pdf", "Tool", "tool"))),
]), cols=2)}
{page_nav((URL["treat"], "Back: Step 2", "Treating Migraine"), (URL["library"], "Next", "Resource Library"), library=False)}
{references(pending(6))}
</main>'''


# =====================================================================================
# 3.4 RESOURCE LIBRARY
# =====================================================================================
def library():
    return f'''<main id="main" class="ja-interior">
{page_hero("After the Yes", "Migraine tools for frontline clinicians", "Browse our free quick guides, guidelines, tools, and videos for frontline migraine care. Filter by step in care, patient group, or format.", eyebrow_href=ATY)}
<section class="ja-section" style="padding-top: 0" aria-label="Resources">
  <div class="ja-container" id="ja-library">
    <form class="ja-filters" aria-label="Filter resources">
      <div class="ja-select-field"><label class="ja-label" for="filter-step">Step in care</label><select class="ja-select" id="filter-step" data-key="step"><option value="all">All steps</option><option value="diag">Diagnosing migraine</option><option value="treat">Treating migraine</option><option value="ongoing">Ongoing care</option></select></div>
      <div class="ja-select-field"><label class="ja-label" for="filter-group">Patient group</label><select class="ja-select" id="filter-group" data-key="group"><option value="all">All patients</option><option value="women">Women’s Health</option><option value="peds">Pediatrics</option><option value="older">Older Adults</option></select></div>
      <div class="ja-select-field"><label class="ja-label" for="filter-format">Format</label><select class="ja-select" id="filter-format" data-key="format"><option value="all">All formats</option><option>Quick Guide</option><option>Guideline</option><option>Tool</option><option>Article</option><option>Video</option><option>Podcast</option></select></div>
    </form>
    <div class="ja-results-bar"><p class="ja-results-count" aria-live="polite"></p><button type="button" class="ja-text-button" data-ja-clear hidden>Clear filters</button></div>
    <div class="ja-empty" hidden><span class="ja-pattern ja-empty__mark" aria-hidden="true"></span><p class="ja-h3">No resources match these filters</p><p class="ja-body">Change a filter to see more, or start again.</p><button type="button" class="ja-text-button" data-ja-clear>Clear filters</button></div>
    <div class="ja-results"></div>
    <noscript><p class="ja-body">Turn on JavaScript to browse and filter the library.</p></noscript>
  </div>
</section>
<script>window.JA_LIBRARY = {LIBRARY_JSON};</script>
</main>'''


# =====================================================================================
# 4.0 CONTACT + THANK YOU
# =====================================================================================
def field(id_, label, typ="text", auto="off", required=True, hint="", textarea=False, err=""):
    h = f' <span class="ja-field__hint">{hint}</span>' if hint else ""
    req = ' required' if required else ""
    e = f' data-error="{err}"' if err else ""
    ctl = (f'<textarea class="ja-input" id="{id_}" name="{id_}"{req}{e}></textarea>' if textarea else
           f'<input class="ja-input" id="{id_}" name="{id_}" type="{typ}" autocomplete="{auto}"{req}{e}>')
    return f'<div class="ja-field"><label class="ja-field__label" for="{id_}">{label}{h}</label>{ctl}</div>'


def contact():
    socials = "".join(f'<li><a class="ja-social__link" href="{url}" aria-label="American Headache Society on {name}">{svg}</a></li>' for name, url, svg in SOCIAL)
    return f'''<main id="main" class="ja-interior">
{page_hero(None, "Contact us", "Questions about Just Ask or the resources on this site? Send us a message and our team will get back to you.")}
<section class="ja-section ja-contact-section ja-contact-section--last" style="padding-top: 0">
  <div class="ja-container ja-contact">
    <aside class="ja-contact__aside"><h2 class="ja-label">Social media</h2><ul class="ja-social">{socials}</ul></aside>
    <form class="ja-form" id="ja-contact-form" action="/contact/thank-you/" method="get" novalidate>
      <div class="ja-form-alert" role="alert" tabindex="-1" hidden><p class="ja-body ja-form-alert__title"></p><ul class="ja-body"></ul></div>
      <div class="ja-form__row">{field("name", "Name", auto="name", err="Enter your name")}{field("email", "Email", "email", "email", err="Enter an email address like name@example.com")}</div>
      <div class="ja-form__row">{field("phone", "Phone number", "tel", "tel", required=False, hint="(optional)")}{field("subject", "Subject", err="Enter a subject")}</div>
      {field("message", "Message", textarea=True, err="Enter a message")}
      <div class="ja-form__actions"><button type="submit" class="ja-button">Send Message</button></div>
    </form>
  </div>
</section>
</main>'''


def thank_you():
    return f'''<main id="main" class="ja-interior">
{page_hero(None, "Thank you", "We’ll get back to you within the next 24 hours.")}
<section class="ja-section" style="padding-top: 0"><div class="ja-container">{button("Back to the Homepage", "/")}</div></section>
</main>'''


# =====================================================================================
# 5.x LEGAL + 404
# =====================================================================================
C = "American Headache Society"


def terms():
    body = f'''<p class="ja-rich__updated">Last updated [date]</p>
<h2>1. Terms</h2>
<p>By accessing this website, you are agreeing to be bound by these terms of service, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using or accessing this site. The materials contained in this website are protected by applicable copyright and trademark law.</p>
<h2>2. Use License</h2>
<ol>
<li>Permission is granted to temporarily download one copy of the materials (information or software) on {C}’s website for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:
<ol type="a"><li>modify or copy the materials;</li><li>use the materials for any commercial purpose, or for any public display (commercial or non-commercial);</li><li>attempt to decompile or reverse engineer any software contained on {C}’s website;</li><li>remove any copyright or other proprietary notations from the materials; or</li><li>transfer the materials to another person or “mirror” the materials on any other server.</li></ol></li>
<li>This license shall automatically terminate if you violate any of these restrictions and may be terminated by {C} at any time. Upon terminating your viewing of these materials or upon the termination of this license, you must destroy any downloaded materials in your possession whether in electronic or printed format.</li>
</ol>
<h2>3. Disclaimer</h2>
<ol>
<li>The materials on {C}’s website are provided on an ‘as is’ basis. {C} makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</li>
<li>Further, {C} does not warrant or make any representations concerning the accuracy, likely results, or reliability of the use of the materials on its website or otherwise relating to such materials or on any sites linked to this site.</li>
</ol>
<h2>4. Limitations</h2>
<p>In no event shall {C} or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on {C}’s website, even if {C} or a {C} authorized representative has been notified orally or in writing of the possibility of such damage. Because some jurisdictions do not allow limitations on implied warranties, or limitations of liability for consequential or incidental damages, these limitations may not apply to you.</p>
<h2>5. Accuracy of Materials</h2>
<p>The materials appearing on {C}’s website could include technical, typographical, or photographic errors. {C} does not warrant that any of the materials on its website are accurate, complete or current. {C} may make changes to the materials contained on its website at any time without notice. However {C} does not make any commitment to update the materials.</p>
<h2>6. Links</h2>
<p>{C} has not reviewed all of the sites linked to its website and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by {C} of the site. Use of any such linked website is at the user’s own risk.</p>
<h2>7. Modifications</h2>
<p>{C} may revise these terms of service for its website at any time without notice. By using this website you are agreeing to be bound by the then current version of these terms of service.</p>
<h2>8. Governing Law</h2>
<p>These terms and conditions are governed by and construed in accordance with the laws of Pennsylvania and you irrevocably submit to the exclusive jurisdiction of the courts in that State or location.</p>
<p>Questions? <a href="/contact/">Contact us</a>.</p>'''
    return legal("Terms & conditions", body)


def privacy():
    body = '''<p class="ja-rich__updated">Last updated [date]</p>
<h2>Third-party advertisers</h2>
<p>We may use third-party advertising to serve ads when you visit other websites. These companies may use information about your visits to this and other websites in order to provide advertisements that are customized to your interests and preferences. These advertisements may appear on other websites. Please note that some of the advertisers on our website and our ad service providers (including advertising network providers and third party ad servers) may deploy cookies or related technologies through their advertising banners, links or other ads. While we use cookies on parts of our site (as discussed above), information received from cookies and other technologies deployed through third party ads and links may be collected directly by those advertisers and ad service providers. The advertiser’s privacy policy and/or that of its service provider will govern the use of this information and we are not responsible for the privacy practices of such companies. Additionally, some of these companies (like the ad networks) are members of the industry group, the Network Advertising Initiative, which offers a single location to opt out of their cookies.</p>
<h2>Security</h2>
<p>While we strive to protect the security and integrity of the information provided to us, due to the inherent nature of the Internet as an open global communications vehicle, we cannot guarantee that information, during transmission through the Internet or while stored on our system or otherwise in our care, will be absolutely safe from intrusion by others, such as hackers.</p>
<p>In the unlikely event that we believe that the security of your information in our possession or control may have been compromised, we may seek to notify you of that development. If a notification is appropriate, we would endeavor to do so as promptly as possible under the circumstances, and, to the extent we have your email address, we may notify you by email. Unless you provide us with another method to notify you in this situation, you consent to our use of e-mail as a means of such notification.</p>
<h2>Third-party ‘linked-to’ websites</h2>
<p>Our website may contain links, banners, or widgets that lead to other sites. We are not responsible for these other sites, and so their posted privacy policies will govern the collection and use of your information on them. We encourage you to read the privacy statements of sites you visit after leaving our website to learn about how your information is treated.</p>
<p>Questions? <a href="/contact/">Contact us</a>.</p>'''
    return legal("Privacy policy", body)


def legal(title, body):
    return f'''<main id="main" class="ja-interior">
{page_hero(None, title, None)}
<section class="ja-section" style="padding-top: 0"><div class="ja-container"><div class="ja-rich ja-body">{body}</div></div></section>
</main>'''


def not_found():
    items = "".join(f'<li style="padding-left: 0">{link(t, h)}</li>' for t, h in [("Go to the Homepage", "/"), ("After the Yes: Guidance and Resources", URL["aty"]), ("Browse the Resource Library", URL["library"])])
    return f'''<main id="main" class="ja-interior">
{page_hero(None, "Page not found", "The page you’re looking for may have moved or no longer exists. Try one of these instead.")}
<section class="ja-section" style="padding-top: 0"><div class="ja-container"><ul class="ja-list" style="gap: 8px">{items}</ul></div></section>
</main>'''


PAGES = [
    dict(key="home", path="index.html", body=home, title="Just Ask: One Question to Help Identify Migraine",
         desc="Migraine affects millions of Americans, and many never get a diagnosis. See how one question, asked of every patient, can bring migraine into the open."),
    dict(key="why", path="why-ask/index.html", body=why_ask, title="Why Ask About Migraine: Closing the Diagnosis Gap",
         desc="Learn why migraine so often goes undiagnosed, what frontline clinicians told AHS, and how one routine question can help close the migraine diagnosis gap."),
    dict(key="ask", path="the-ask/index.html", body=the_ask, title="A One-Question Migraine Screen for Every Patient",
         desc="One question, asked of every patient, can surface migraine that often goes undiagnosed. Learn why it works and how to fit it into your workflow."),
    dict(key="aty", path="after-the-yes/index.html", body=after_the_yes, title="What to Do After a Patient Says Yes to Migraine Screening",
         desc="A yes opens the path to diagnosis. Get clear next steps for diagnosing, treating, and following up on migraine in frontline care, with resources from AHS."),
    dict(key="diag", path="after-the-yes/diagnosing-migraine/index.html", body=diagnosing, title="Diagnosing Migraine: Screening and Red Flags",
         desc="Use the ID Migraine screen, core diagnostic features, and red flags to diagnose migraine with confidence, then talk with your patient about next steps."),
    dict(key="treat", path="after-the-yes/treating-migraine/index.html", body=treating, title="Treating Migraine: Acute and Preventive Options",
         desc="Match acute treatment to migraine severity, know when to add preventive treatment, and get through prior authorization with practical tools from AHS."),
    dict(key="ongoing", path="after-the-yes/ongoing-migraine-care/index.html", body=ongoing, title="Ongoing Migraine Care: Follow-Up and Referral",
         desc="Know when to reassess migraine treatment, what to review at each visit, and how to use e-consults and referrals while your patient stays in your care."),
    dict(key="library", path="resources/index.html", body=library, title="Migraine Resource Library for Clinicians",
         desc="Get free guides, guidelines, tools, and videos to diagnose, treat, and follow up on migraine. Filter by step in care, patient group, or format."),
    dict(key="contact", path="contact/index.html", body=contact, title="Contact", desc="Contact the Just Ask. campaign team at the American Headache Society."),
    dict(key="thanks", path="contact/thank-you/index.html", body=thank_you, title="Thank You", desc="Thanks for contacting the Just Ask. team.", noindex=True),
    dict(key="terms", path="terms/index.html", body=terms, title="Terms & Conditions", desc="Terms and conditions for the Just Ask. website.", noindex=True),
    dict(key="privacy", path="privacy/index.html", body=privacy, title="Privacy Policy", desc="Privacy policy for the Just Ask. website.", noindex=True),
    dict(key="404", path="404.html", body=not_found, title="Page Not Found", desc="This page could not be found.", noindex=True),
]
