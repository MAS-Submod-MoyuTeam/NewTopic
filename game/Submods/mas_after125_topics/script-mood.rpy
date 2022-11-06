init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mas_mood_insecure",
            prompt="...不安全.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mas_mood_loved",
            prompt="...被爱着.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mas_mood_guilty",
            prompt="...内疚.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label mas_mood_loved:
    m 1ekbla "那我的心思就隔着屏幕传给你了..."
    m 3hubsb "毕竟我比什么都爱你!"
    if has_family and persistent._mas_pm_has_friends:
        $ fnf_str = "家人和朋友"
    elif has_family:
        $ fnf_str = "家人"
    else:
        $ fnf_str = "朋友"
    m 3eub "当然爱你的也不止我, 还有你的[fnf_str]!"
    m 1dkbsa "你能有再多的爱都不过分, {w=0.1}{nw}"
    extend 1ekbsu "也肯定会有我那一份的, [mas_get_player_nickname()]~"
    return "love"

label mas_mood_insecure:
    m 2dkc "..."
    m 2eka "引用一句夏树喜欢的漫画吧..."
    m 7dku "'你相信我, 相信我相信你.'"
    m 3eka "我就是这个意思."
    m 3ekbsa "要是相信不了自己了, 那就相信我."
    m 1eubsu "因为我, {w=0.1}当然会相信你{w=0.1}能穿过一切迷惘的~"
    return
    
label mas_mood_guilty:
    m 2wkd "[player]!"
    m 2dkc "我们都有犯错的时候... {w=0.3}{nw}"
    extend 7eka "也肯定有被原谅的理由."
    m 3dku "毕竟你是个这么好的人... {w=0.3}{nw}"
    extend 1eka "友善, 热忱, 忠实于自己."
    m 1dua "你已经有承认错误的勇气了, 现在翻过这一页就好."
    m 1ekbsu "我爱你.{w=0.2} 也记得要善待自己, 好吗?"
    return
