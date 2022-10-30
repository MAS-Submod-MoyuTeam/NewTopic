init 5 python:
    ev_rules = dict()
    ev_rules.update(
        MASGreetingRule.create_rule(
            skip_visual=True,
            random_chance=10,
            override_type=True
        )
    )

    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_found_nou_shirt",
            conditional=(
                "mas_getAbsenceLength() >= datetime.timedelta(hours=3) "
                "and mas_nou.get_wins_for('Player') > {0} "
                "and mas_nou.get_total_games() > {1} "
                "and not mas_isSpecialDay() "
                "and not mas_SELisUnlocked(mas_clothes_nou_shirt)"
            ).format(random.randint(45, 65), random.randint(95, 115)),
            unlocked=True,
            rules=ev_rules,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="GRE"
    )

    del ev_rules

default persistent._mas_pm_snitched_on_chibika = None

label greeting_found_nou_shirt:
    python:
        mas_RaiseShield_core()
        mas_startupWeather()
        monika_chr.change_clothes(mas_clothes_nou_shirt, by_user=False, outfit_mode=True)
        glitch_option_text = glitchtext(7)

    call spaceroom(hide_monika=True, dissolve_all=True, scene_change=True, show_emptydesk=True)
    pause 2.5

    m "你来啦! {w=0.2}我等你好久了~"
    m "呃, 我是不知道你怎么偷偷把这个塞给我的, [player]...{nw}"
    $ _history_list.pop()
    show screen mas_background_timed_jump(5, "greeting_found_nou_shirt.menu_skip")
    menu:
        m "呃, 我是不知道你怎么偷偷把这个塞给我的, [player]...{fast}"

        "是秘密.":
            hide screen mas_background_timed_jump
            jump greeting_found_nou_shirt.menu_choice_secret

        "是 [glitch_option_text] 教我的!":
            hide screen mas_background_timed_jump
            $ persistent._mas_pm_snitched_on_chibika = True
            $ renpy.invoke_in_thread(
                mas_utils.trywrite,
                os.path.join(renpy.config.basedir, "characters/for snitch.txt"),
                ">:("
            )
            jump greeting_found_nou_shirt.menu_choice_other

        "我也不知道...":
            hide screen mas_background_timed_jump
            jump greeting_found_nou_shirt.menu_choice_other

    label .post_menu:
        pass

    m 1ekbla "谢啦, [player]."
    m 1tfu "别以为换件衣服我就会让着你哦~"

    if mas_nou.get_wins_for('Player') >= mas_nou.get_wins_for('Monika'):
        m 1rtsdlb "其实, {w=0.1}我还不如再认真点玩, 哈哈..."

    m 3ttb "想来一局了吗, [mas_get_player_nickname()]?"

    python:
        mas_selspr.unlock_clothes(mas_clothes_nou_shirt)
        mas_selspr.save_selectables()
        mas_lockEVL("greeting_found_nou_shirt", "GRE")
        renpy.save_persistent()

        del glitch_option_text

        mas_MUINDropShield()
        set_keymaps()
        HKBShowButtons()
        mas_startup_song()
        enable_esc()
    return

label greeting_found_nou_shirt.menu_skip:
    hide screen mas_background_timed_jump
    call mas_transition_from_emptydesk("monika 4sub")
    m "不过我喜欢哦~"

    jump greeting_found_nou_shirt.post_menu

label greeting_found_nou_shirt.menu_choice_secret:
    if mas_isMoniEnamored(higher=True):
        call mas_transition_from_emptydesk("monika 2tublu")
        m "{cps=*1.5}你不会是{i}经常{/i}去偷看我的衣柜吧?~{/cps}{w=0.1}{nw}"
        $ _history_list.pop()
        m 2lusdla "总之...{w=0.3}{nw}"

    else:
        call mas_transition_from_emptydesk("monika 2rtblsdlu")
        m "唔, 总之...{w=0.3}{nw}"

    extend 4sub "我真的好喜欢这身!"

    jump greeting_found_nou_shirt.post_menu

label greeting_found_nou_shirt.menu_choice_other:
    show noise zorder 500 onlayer overlay:
        alpha 0.0
        easein_elastic 0.5 alpha 0.1
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide noise onlayer overlay

    jump greeting_found_nou_shirt.menu_skip