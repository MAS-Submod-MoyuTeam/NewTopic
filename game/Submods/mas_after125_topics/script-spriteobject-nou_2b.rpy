init -2 python in mas_sprites:
    def _clothes_hatana_2b_entry(_moni_chr, **kwargs):
        """
        Entry pp for hatana 2b
        """
        outfit_mode = kwargs.get("outfit_mode", False)

        if outfit_mode:
            # swap to echo_downshort hair if found, if not, hair_down
            downshort = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_HAIR,
                "echo_downshort"
            )
            _moni_chr.change_hair(downshort if downshort is not None else store.mas_hair_down)

        # remove promise ring so it can't cli[ thru gloves
        _acs_remove_if_found(_moni_chr, "promisering")


    def _clothes_hatana_2b_exit(_moni_chr, **kwargs):
        """
        Exit prog point for hatana 2b
        """
        # re-wear promise ring if applicable
        if store.persistent._mas_acs_enable_promisering:
            _moni_chr.wear_acs(store.mas_acs_promisering)

init -1 python:
    mas_clothes_nou_shirt = MASClothes(
        "nou_shirt",
        "nou_shirt",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_C_DTS: True
        },
        pose_arms=MASPoseArms(
            {
                9: MASArmRight(
                    "def",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        )
    )
    store.mas_sprites.init_clothes(mas_clothes_nou_shirt)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_nou_shirt,
        "Shirt (NOU)",
        "nou_shirt",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            "No U! Ehehe~",
            "Ready to draw some more cards?~",
            "Colorful!",
            "Plus 10 to luck~",
            "Up for a game, [player]?"
        ]
    )