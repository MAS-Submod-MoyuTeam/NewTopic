init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_o31_hatana_2b",
            category=[store.mas_greetings.TYPE_HOL_O31]
        ),
        code="GRE"
    )

label greeting_o31_hatana_2b:
    call spaceroom(hide_monika=True, scene_change=True, dissolve_all=True)
    #moni is off-screen

    if persistent._mas_o31_relaunch:
        m "Almost ready, [player]..."
        m "I just hope this skirt doesn't self-destruct."
        m "{cps=*2}Although maybe you do...{/cps}{nw}"
        $ _history_list.pop()
        m "Okay, there. {w=0.2}Ready [player]?"

    else:
        m "Okay there, {w=0.1}I think that's everything."
        m "Just as long as this skirt doesn't self-destruct...{w=0.3}that'd be really embarrassing!"
        m "Oh! {w=0.2}I think I hear something..."
        m "[player]?"

    m "I have a question for you..."
    m "To be..."

    #show moni now
    call mas_transition_from_emptydesk("monika 3hub")

    m 3hub "...or not 2B?!"
    m 1hub "Ahaha!"
    m 2eka "So, what do you think?"
    m 2hub "I think it's a really cool costume, thanks again for giving it to me!"
    m 7rtu "Say [player], have I ever told you there is something calming about you?"
    m 3euu "Well, I just wanted you to know that. {w=0.2}{nw}"
    extend 3tuu "Hopefully it never gets wiped from your memory."
    m 3eud "That reminds me, make sure you back up my data from time to time, I'd do the same for you if I could..."
    m 1hksdlb "Oh gosh, I'm not even sure what that means, I'm just rambling now, ahaha!"

    call greeting_o31_deco
    call greeting_o31_cleanup
    return