def on_button_pressed_a():
    global cookies
    cookies += click_power
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global cookies, cps, factory_price
    if cookies >= factory_price:
        cookies += -1 * factory_price
        cps += factory_power
        factory_price += Math.round(factory_price / 2)
    else:
        basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    global upgrade_loop, Upgrade_no_2, upgrade_no, click_power, upgrade_price, cps_multi, gma_power, Farm_power, mine_power, factory_power, cookies
    if cookies == upgrade_price:
        if upgrade_loop == 0:
            upgrade_loop += 1
            Upgrade_no_2 += 1
            upgrade_no = Upgrade_no_2
        else:
            Upgrade_no_2 += 1
            upgrade_loop = 0
            upgrade_no = 2
        click_power += 1
        upgrade_price += 100
        if upgrade_no == 1:
            click_power += click_power
        elif upgrade_no == 2:
            cps_multi += cps_multi / 5
        elif upgrade_no == 3:
            gma_power += gma_power
        elif upgrade_no == 5:
            click_power += click_power
        elif upgrade_no == 7:
            Farm_power += Farm_power
        elif upgrade_no == 9:
            click_power += click_power
        elif upgrade_no == 11:
            mine_power += mine_power
        elif upgrade_no == 13:
            click_power += click_power
        elif upgrade_no == 15:
            factory_power += factory_power
        cookies += upgrade_price * -1
    else:
        basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global cookies, cps, gma_price
    if cookies >= gma_price:
        cookies += -1 * gma_price
        cps += gma_power
        gma_price += Math.round(gma_price / 2)
    else:
        basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global cookies, cps, Farm_price
    if cookies >= Farm_price:
        cookies += -1 * Farm_price
        cps += Farm_power
        Farm_price += Math.round(Farm_price / 2)
    else:
        basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    global cookies, cps, mine_price
    if cookies >= mine_price:
        cookies += -1 * mine_price
        cps += mine_power
        mine_price += Math.round(mine_price / 2)
    else:
        basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    global cookies, cps, bank_price
    if cookies >= bank_price:
        cookies += -1 * bank_price
        cps += bank_power
        bank_price += Math.round(bank_price / 2)
    else:
        basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

upgrade_loop = 0
bank_power = 0
bank_price = 0
factory_power = 0
factory_price = 0
mine_power = 0
mine_price = 0
Farm_price = 0
gma_power = 0
upgrade_no = 0
cookies = 0
gma_price = 0
click_power = 0
upgrade_price = 0
cps_multi = 0
Upgrade_no_2 = 0
Farm_power = 0
Farm_power = 8
Upgrade_no_2 = 0
cps_multi = 1
cps_total = 0
upgrade_price = 100
click_power = 1
gma_price = 20
cps = 0
cookies = 0
upgrade_no = 0
gma_power = 1
Farm_price = 1100
mine_price = 12000
mine_power = 50
factory_price = 130000
factory_power = 260
bank_price = 1400000
bank_power = 1400
gold_cookie = False

def on_every_interval():
    global gold_cookie
    gold_cookie = True
    basic.pause(10000)
    gold_cookie = False
loops.every_interval(randint(180000, 300000), on_every_interval)

def on_forever():
    global cps_total, cookies
    cps_total = cps * cps_multi
    cookies += cps_total
    if gold_cookie == True:
        basic.show_string("!G!")
        basic.show_number(cookies)
    else:
        basic.show_number(cookies)
basic.forever(on_forever)
