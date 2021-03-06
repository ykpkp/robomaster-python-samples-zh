def start():
    云台.设置旋转速度(30)

    print('no move')
    云台灯(常量.云台所有, 红色, 常量.效果常亮)
    大师.设置模式(常量.云台跟随模式)
    云台.平转(90)
    时间.睡眠(3)

    print('only gimbal move')
    云台灯(常量.云台所有, 黄色, 常量.效果走马灯)
    大师.设置模式(常量.自由模式)
    云台.平转(90)

    print('both move')
    云台灯(常量.云台所有, 绿色, 常量.效果闪烁)
    大师.设置模式(常量.底盘跟随模式)
    云台.平转(-90)

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

# 常量部分
常量 = rm_define
常量.底盘跟随模式 = 常量.robot_mode_chassis_follow
常量.云台跟随模式 = 常量.robot_mode_gimbal_follow
常量.自由模式 = 常量.robot_mode_free

常量.云台所有 = 常量.armor_top_all
常量.云台左 = 常量.armor_top_left
常量.云台右 = 常量.armor_top_right

常量.效果常亮 = 常量.effect_always_on
常量.效果熄灭 = 常量.effect_always_off
常量.效果呼吸 = 常量.effect_breath
常量.效果闪烁 = 常量.effect_flash
常量.效果走马灯 = 常量.effect_marquee

时间 = time
时间.睡眠 = 时间.sleep