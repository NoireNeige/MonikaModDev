# deco testing


image dev_monika_bg_one = "dev/deco/fakebg_1.png"
image dev_monika_bg_two = "dev/deco/fakebg_2.png"
image dev_monika_bg_thr = "dev/deco/fakebg_3.png"
image dev_monika_deco_one = "dev/deco/fakedeco_1_0.png"
image dev_monika_deco_one_alt = "dev/deco/fakedeco_1_0_alt.png"
image dev_monika_deco_two = "dev/deco/fakedeco_2_0.png"
image dev_monika_deco_thr = "dev/deco/fakedeco_3_0.png"

image dev_monika_deco_flt = MASFilterSwitch("dev/deco/fakedeco_1_2.png")


init -1 python:
    dev_mas_bg_1 = MASFilterableBackground(
        "dev_mas_bg_1",
        "Fake BG 1",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_one",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_one",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_one",
            }),
        ),
        store.mas_background.default_MBGFM(),
        unlocked=True
    )
    dev_mas_bg_2 = MASFilterableBackground(
        "dev_mas_bg_2",
        "Fake BG 2",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_two",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_two",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_two",
            }),
        ),
        store.mas_background.default_MBGFM(),
        unlocked=True
    )
    dev_mas_bg_3 = MASFilterableBackground(
        "dev_mas_bg_3",
        "Fake BG 3",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_thr",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_thr",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "dev_monika_bg_thr",
            }),
        ),
        store.mas_background.default_MBGFM(),
        unlocked=True
    )


init 501 python:

    # uncoment this to test register_img_same init exception
#    MASImageTagDecoDefinition.register_img_same(
#        "dev_monika_deco_one",
#        store.mas_background.MBG_DEF,
#        "dev_mas_bg_1"
#    )

    # spaceroom will be default position
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_one",
        store.mas_background.MBG_DEF,
        MASAdvancedDecoFrame(zorder=6)
    )
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_two",
        store.mas_background.MBG_DEF,
        MASAdvancedDecoFrame(zorder=6)
    )
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_thr",
        store.mas_background.MBG_DEF,
        MASAdvancedDecoFrame(zorder=6)
    )

    # fake bg 1
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_one",
        "dev_mas_bg_1",
        MASAdvancedDecoFrame(at_list=[i44], zorder=6),
    )
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_two",
        "dev_mas_bg_1",
        MASAdvancedDecoFrame(at_list=[i31], zorder=6)
    )
    MASImageTagDecoDefinition.register_img_same(
        "dev_monika_deco_thr",
        store.mas_background.MBG_DEF,
        "dev_mas_bg_1"
    )

    # fake bg 2
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_one",
        "dev_mas_bg_2",
        MASAdvancedDecoFrame(zorder=6),
        replace_tag="dev_monika_deco_one_alt"
    )
    #MASImageTagDecoDefinition.register_img(
    #    "dev_monika_deco_two",
    #    "dev_mas_bg_2",
    #    MASAdvancedDecoFrame(at_list=[i33], zorder=6)
    #)
    MASImageTagDecoDefinition.register_img(
        "dev_monika_deco_flt",
        "dev_mas_bg_2",
        MASAdvancedDecoFrame(zorder=20)
    )
    MASImageTagDecoDefinition.register_img_same(
        "dev_monika_deco_thr",
        store.mas_background.MBG_DEF,
        "dev_mas_bg_2"
    )


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dev_deco_tag_test_api",
            category=["dev"],
            prompt="DECO TAG TEST API REG",
            pool=True,
            unlocked=True
        )
    )

label dev_deco_tag_test_api:

    m 1eub "TIME TO TEST deco API and bg change"

    m 1eua "I am going to show an image, but it will appear when i change BG"
    $ mas_showDecoTag("dev_monika_deco_one")
    m 1euc "image added"
    call mas_background_change(dev_mas_bg_1, skip_leadin=True, skip_outro=True)
    m 1eua "image should be visible now"

    $ mas_hideDecoTag("dev_monika_deco_one")
    m 1euc "image removed, but only when the BG changes"
    call mas_background_change(dev_mas_bg_2, skip_leadin=True, skip_outro=True)
    m 1eub "image should be gone now"

    m 1euc "now i will show image right away"
    $ mas_showDecoTag("dev_monika_deco_one", show_now=True)
    m 1eub "should be visible now"

    call mas_background_change(dev_mas_bg_1, skip_leadin=True, skip_outro=True)
    m 1euc "image should still be visible, but in different position"
    $ mas_hideDecoTag("dev_monika_deco_one", hide_now=True)
    m 1eud "should be hidden now"

    call mas_background_change(mas_background_def, skip_leadin=True, skip_outro=True)
    m 1eub "should still be hidden"

    m 1euc "now I am going set deco to be shown, but not right away"
    $ mas_showDecoTag("dev_monika_deco_one")
    m 1eua "and now i am going to call spaceroom, no scene change"
    call spaceroom()

    m 2eua "the deco should be shown now"
    m 1eub "and now i will set deco to be hidden, but not right away"
    $ mas_hideDecoTag("dev_monika_deco_one")
    m 1eua "and now I am gonig to call spaceroom, no scene change"
    call spaceroom()

    m 2eua "deco should be hidden now"
    m 6wuw "thanks"

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dev_deco_tag_test_api_same",
            category=["dev"],
            prompt="DECO TAG TEST API REG SAME",
            pool=True,
            unlocked=True
        )
    )

label dev_deco_tag_test_api_same:
    
    m 1eub "TIME TO TEST `register_img_same`"
    $ mas_showDecoTag("dev_monika_deco_thr", show_now=True)

    m "a blue deco whould be visible"
    call mas_background_change(dev_mas_bg_1, skip_leadin=True, skip_outro=True)
    m "the deco should be in the same place"

    call mas_background_change(dev_mas_bg_2, skip_leadin=True, skip_outro=True)
    m 1eua "the deco should STILL be in the same place"

    $ mas_hideDecoTag("dev_monika_deco_thr")
    call mas_background_change(mas_background_def, skip_leadin=True, skip_outro=True)
    m 2eub "deco should be hideen now"
    m 6wuw "Thanks"

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dev_deco_tag_test_adf",
            category=["dev"],
            prompt="DECO TAG TEST ADF",
            pool=True,
            unlocked=True
        )
    )

label dev_deco_tag_test_adf:

    m 1eub "I am going to add deco and cycle bgs"
    $ mas_showDecoTag("dev_monika_deco_one", show_now=True)
    $ mas_showDecoTag("dev_monika_deco_two", show_now=True)

    m 1eua "both are visible. Now to go to fake bg 1"
    call mas_background_change(dev_mas_bg_1)

    m 1eub " they should be in different positions"
    m 1euc " now to next bg"
    call mas_background_change(dev_mas_bg_2)

    m 1eud "deco 1 should be a different color, deco 2 should be hidden"
    m 2wuw "now back to spaceroom"
    call mas_background_change(mas_background_def)

    m 6wuw "yay"
    m 1eua "and hide decos now"
    $ mas_hideDecoTag("dev_monika_deco_one", hide_now=True)
    $ mas_hideDecoTag("dev_monika_deco_two", hide_now=True)

    m 6wuw "thanks"

    return
