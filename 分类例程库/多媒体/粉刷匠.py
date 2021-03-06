def start():
    单位间隔 = 16/64
    乐谱 = [
        常量.嗦1, 1, 常量.咪1, 1, 常量.嗦1, 1, 常量.咪1, 1, 常量.嗦1, 1, 常量.咪1, 1, 常量.哆1, 2,
        常量.来1, 1, 常量.发1, 1, 常量.咪1, 1, 常量.来1, 1, 常量.嗦1, 4,
        常量.嗦1, 1, 常量.咪1, 1, 常量.嗦1, 1, 常量.咪1, 1, 常量.嗦1, 1, 常量.咪1, 1, 常量.哆1, 2,
        常量.来1, 1, 常量.发1, 1, 常量.咪1, 1, 常量.来1, 1, 常量.哆1, 4,
        常量.来1, 1, 常量.来1, 1, 常量.发1, 1, 常量.发1, 1, 常量.咪1, 1, 常量.来1, 1, 常量.嗦1, 2,
        常量.来1, 1, 常量.发1, 1, 常量.咪1, 1, 常量.来1, 1, 常量.嗦1, 4,
        常量.嗦1, 1, 常量.咪1, 1, 常量.嗦1, 1, 常量.咪1, 1, 常量.嗦1, 1, 常量.咪1, 1, 常量.哆1, 2,
        常量.来1, 1, 常量.发1, 1, 常量.咪1, 1, 常量.来1, 1, 常量.哆1, 4
    ]

    #云台灯(常量.云台所有, 绿色, 常量.效果闪烁)
    for 序号 in range(0, len(乐谱)):
        if 序号 % 2 == 0:
            多媒体.演奏(乐谱[序号])
        else:
            时间.睡眠(乐谱[序号] * 单位间隔)

    print(str(工具.程序运行时间()) + " seconds")

def 云台灯(位置, 颜色, 灯效):
    LED灯.云台(位置, 颜色['红'], 颜色['绿'], 颜色['蓝'], 灯效)

白色 = {'红': 255, '绿': 255, '蓝': 255}
黑色 = {'红': 0, '绿': 0, '蓝': 0}
黄色 = {'红': 255, '绿': 255, '蓝': 0}
红色 = {'红': 255, '绿': 0, '蓝': 0}
绿色 = {'红': 0, '绿': 255, '蓝': 0}
蓝色 = {'红': 0, '绿': 0, '蓝': 255}

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.
LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl
云台.旋转 = 云台.rotate

工具 = tools
工具.累计计时 = 工具.timer_current
工具.程序运行时间 = 工具.run_time_of_program
工具.计时器 = 工具.timer_ctrl

多媒体 = media_ctrl
多媒体.演奏 = 多媒体.play_sound

时间 = time
时间.睡眠 = 时间.sleep

# 常量部分
常量 = rm_define
常量.底盘跟随模式 = 常量.robot_mode_chassis_follow
常量.云台跟随模式 = 常量.robot_mode_gimbal_follow
常量.自由模式 = 常量.robot_mode_free

常量.云台所有 = 常量.armor_top_all
常量.云台左 = 常量.armor_top_left
常量.云台右 = 常量.armor_top_right

常量.云台向左 = 常量.gimbal_left

常量.效果常亮 = 常量.effect_always_on
常量.效果熄灭 = 常量.effect_always_off
常量.效果呼吸 = 常量.effect_breath
常量.效果闪烁 = 常量.effect_flash
常量.效果走马灯 = 常量.effect_marquee

常量.开始 = 常量.timer_start
常量.暂停 = 常量.timer_stop
常量.重置 = 常量.timer_reset

常量.哆1 = 常量.media_sound_solmization_1C
常量.来1 = 常量.media_sound_solmization_1D
常量.咪1 = 常量.media_sound_solmization_1E
常量.发1 = 常量.media_sound_solmization_1F
常量.嗦1 = 常量.media_sound_solmization_1G
常量.啦1 = 常量.media_sound_solmization_1A
常量.西1 = 常量.media_sound_solmization_1B

常量.哆2 = 常量.media_sound_solmization_2C
常量.来2 = 常量.media_sound_solmization_2D
常量.咪2 = 常量.media_sound_solmization_2E
常量.发2 = 常量.media_sound_solmization_2F
常量.嗦2 = 常量.media_sound_solmization_2G
常量.啦2 = 常量.media_sound_solmization_2A
常量.西2 = 常量.media_sound_solmization_2B

常量.哆3 = 常量.media_sound_solmization_3C
常量.来3 = 常量.media_sound_solmization_3D
常量.咪3 = 常量.media_sound_solmization_3E
常量.发3 = 常量.media_sound_solmization_3F
常量.嗦3 = 常量.media_sound_solmization_3G
常量.啦3 = 常量.media_sound_solmization_3A
常量.西3 = 常量.media_sound_solmization_3B

