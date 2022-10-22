init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="NewTopic",
        description="为<0.12.5版本提供新版本话题.",
        version='1.23.0',
        settings_pane="newtopic_setting_pane"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="NewTopic",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="NewTopic",
            update_dir="",
            attachment_id=None
        )

# 检测新版本 用于mas_after125_topics
init -995 python:
    import os
    import shutil
    DP_NEW_VERSION=['0', '12', '5']
    splitver = renpy.config.version.split('.')
    DP_CURR_VERSION = [splitver[0], splitver[1], splitver[2]]
    p_is_old_ver = store.mas_utils.compareVersionLists(DP_CURR_VERSION, DP_NEW_VERSION) == -1
    #-1 0 1

screen newtopic_setting_pane():
    if p_is_old_ver:
        label "检测到为旧版本，功能正常启用"
    else:
        label "检测到为新版本，不进行加载"