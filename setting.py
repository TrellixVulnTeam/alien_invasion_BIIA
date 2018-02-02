import pygame


class Settings():
    # 配置游戏所有的设置数据
    def __init__(self):
        #  初始化游戏的静态设置
        #  屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.mouse_image_filename = "images/mouse.png"
        self.full_screen = False
        self.flags = 0  # 全屏参数
        self.window_width = self.screen_width
        self.window_height = self.screen_height
        #  标题栏高度
        self.score_bar_height = 0
        #  标题设置
        self.game_title = "小可爱打猪大叔"
        #  游戏信息存储文件路径设置
        self.info_file = "game_info.json"
        # 定义画面帧率
        self.FRAME_RATE = 600
        # 定义动画周期（帧数）
        self.ANIMATE_CYCLE = 600
        # 定义画面帧标示
        self.ticks = 0
        #  声音设置声音
        self.begin_audio_file = 'audio/ready_go.wav'
        self.begin_audio = pygame.mixer.Sound(self.begin_audio_file)
        self.begin_audio_channel = pygame.mixer.Channel(1)
        self.ship_hit_audio_file = 'audio/explo.wav'
        self.ship_hit_audio = pygame.mixer.Sound(self.ship_hit_audio_file)
        self.ship_hit_audio_channel = pygame.mixer.Channel(2)
        self.over_audio_file = 'audio/game_over.wav'
        self.over_audio = pygame.mixer.Sound(self.over_audio_file)
        self.over_audio_channel = pygame.mixer.Channel(3)

        #  游戏可玩性参数初始化
        #  飞船设置
        self.ship_speed_factor = 0
        self.ship_limit = 3
        #  子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 255, 60, 60
        self.bullets_allowed = 20
        #  外星人设置
        self.alien_speed_factor = 0
        self.fleet_drop_speed = 0
        self.fleet_direction = 1
        self.alien_points = 0
        #  boss设置
        self.boss_speed_factor = 0
        self.boss_points = 0
        self.MAX_HP = 50
        #  外星人填充程度设置
        self.alien_high_fill_factor = 0.6

        #  加快游戏节奏参数
        # 外星人提高速度
        self.ship_speedup_scale = 1.2
        self.bullet_speedup_scale = 1.15
        self.alien_speedup_scale = 1.15
        # 外星人点数的提高参数
        self.score_scale = 1.2
        # boss加快节奏参数
        self.boss_speedup_scale = 1.5
        self.add_HP_scale = 1.25
        # 外星人点数的提高参数
        self.boss_score_scale = 1.5

    def initialize_dynamic_settings(self):
        #  初始化随游戏进行而变化的设置
        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 0.8
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 8
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1
        self.alien_points = 5
        #  boss设置
        self.boss_speed_factor = 0.5
        self.boss_points = 8
        self.MAX_HP = 20

    def increase_speed(self):
        #  提高速度设置
        self.ship_speed_factor *= self.ship_speedup_scale
        self.bullet_speed_factor *= self.bullet_speedup_scale
        self.alien_speed_factor *= self.alien_speedup_scale
        self.fleet_drop_speed *= self.alien_speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def boss_increase_speed(self):
        #  提高速度设置
        self.boss_speed_factor *= self.boss_speedup_scale
        self.boss_points = int(self.boss_points * self.boss_score_scale)
        #  boss血量
        self.MAX_HP *= self.add_HP_scale
