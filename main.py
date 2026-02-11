def on_button_pressed_a():
    global cookies, gold_action, G_CPS_Multi, G_Click_Multi, gma_power, Farm_power, mine_power, factory_power, bank_power
    if mode == 0:
        cookies += click_power * G_Click_Multi
    elif mode == 0:
        if gold_cookie == True:
            gold_action = randint(0, 7)
        if gold_action == 0:
            G_CPS_Multi = 7
            basic.show_leds("""
                # # . . .
                # . . # .
                # # . . #
                . . . # .
                . . . . .
                """)
            basic.show_leds("""
                . . . . .
                # . . . .
                . . # # #
                # . . # .
                . . # . .
                """)
            basic.pause(77000)
            G_CPS_Multi = 1
        elif gold_action == 1:
            G_Click_Multi = 777
            basic.show_leds("""
                . # . . .
                . # . . .
                # # # # .
                # # # # .
                . # # # .
                """)
            basic.show_string("X777!")
            basic.pause(13000)
            G_Click_Multi = 1
        elif gold_action == 2:
            gma_power += gma_power / 10 * Gma_amount
            basic.pause(13000)
            gma_power += gma_power / 10 * Gma_amount * -1
        elif gold_action == 3:
            Farm_power += Farm_power / 10 * farm_amount
            basic.pause(13000)
            Farm_power += Farm_power / 10 * farm_amount / -1
        elif gold_action == 4:
            mine_power += mine_power / 10 * mine_amount
            basic.pause(13000)
            mine_power += mine_power / 10 * mine_amount * -1
        elif gold_action == 5:
            factory_power += factory_power / 10 * factory_amount
            basic.pause(13000)
            factory_power += factory_power / 10 * factory_amount / -1
        else:
            bank_power += bank_power / 10 * bank_amount
            basic.pause(13000)
            bank_power += bank_power / 10 * bank_amount * -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global upgrade_loop, Upgrade_no_2, upgrade_no, click_power, upgrade_price, cps_multi, gma_power, Farm_power, mine_power, factory_power, cookies, cps, mine_price, mine_amount
    if mode == 0:
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
    elif mode == 1:
        if cookies >= mine_price:
            cookies += -1 * mine_price
            cps += mine_power
            mine_price += Math.round(mine_price / 2)
            mine_amount += 1
        else:
            basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global cookies, cps, gma_price, Gma_amount, Farm_price, farm_amount
    if mode == 0:
        if cookies >= gma_price:
            cookies += -1 * gma_price
            cps += gma_power
            gma_price += Math.round(gma_price / 2)
            Gma_amount += 1
        else:
            basic.show_icon(IconNames.SAD)
    elif mode == 1:
        if cookies >= Farm_price:
            cookies += -1 * Farm_price
            cps += Farm_power
            Farm_price += Math.round(Farm_price / 2)
            farm_amount += 1
        else:
            basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global mode
    if mode == 0:
        mode += 1
        basic.show_string("M2")
    else:
        mode = 0
        basic.show_string("M1")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global cookies, cps, bank_price, bank_amount, factory_price, factory_amount
    if mode == 0:
        if cookies >= bank_price:
            cookies += -1 * bank_price
            cps += bank_power
            bank_price += Math.round(bank_price / 2)
            bank_amount += 1
        else:
            basic.show_icon(IconNames.SAD)
    elif mode == 1:
        if cookies >= factory_price:
            cookies += -1 * factory_price
            cps += factory_power
            factory_price += Math.round(factory_price / 2)
            factory_amount += 1
        else:
            basic.show_icon(IconNames.SAD)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

cps_total = 0
cps = 0
upgrade_loop = 0
gold_action = 0
bank_amount = 0
factory_amount = 0
mine_amount = 0
farm_amount = 0
Gma_amount = 0
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
mode = 0
gold_cookie = False
G_CPS_Multi = 0
G_Click_Multi = 1
G_CPS_Multi = 1
gold_miss = 0
mode = 0
Farm_power = 8
Upgrade_no_2 = 0
cps_multi = 1
upgrade_price = 100
click_power = 1
gma_price = 20
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
Gma_amount = 0
farm_amount = 0
mine_amount = 0
factory_amount = 0
bank_amount = 0

def on_every_interval():
    global gold_miss, gold_cookie
    if gold_miss == 0:
        basic.pause(2000)
        gold_miss += 1
    else:
        gold_cookie = True
        basic.pause(10000)
        gold_cookie = False
loops.every_interval(randint(180000, 300000), on_every_interval)

def on_forever():
    global cps_total, cookies
    if gold_cookie == True:
        cps_total = cps * (cps_multi * G_CPS_Multi)
        cookies += cps_total
        basic.show_string("!G!")
        basic.show_number(cookies)
    else:
        cps_total = cps * (cps_multi * G_CPS_Multi)
        cookies += cps_total
        basic.show_number(cookies)
basic.forever(on_forever)
