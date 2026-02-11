input.onButtonPressed(Button.A, function () {
    if (mode == 0) {
        cookies += click_power * G_Click_Multi
    } else if (mode == 0) {
        if (gold_cookie == true) {
            gold_action = randint(0, 7)
        }
        if (gold_action == 0) {
            G_CPS_Multi = 7
            basic.showLeds(`
                # # . . .
                # . . # .
                # # . . #
                . . . # .
                . . . . .
                `)
            basic.showLeds(`
                . . . . .
                # . . . .
                . . # # #
                # . . # .
                . . # . .
                `)
            basic.pause(77000)
            G_CPS_Multi = 1
        } else if (gold_action == 1) {
            G_Click_Multi = 777
            basic.showLeds(`
                . # . . .
                . # . . .
                # # # # .
                # # # # .
                . # # # .
                `)
            basic.showString("X777!")
            basic.pause(13000)
            G_Click_Multi = 1
        } else if (gold_action == 2) {
            gma_power += gma_power / 10 * Gma_amount
            basic.pause(13000)
            gma_power += gma_power / 10 * Gma_amount * -1
        } else if (gold_action == 3) {
            Farm_power += Farm_power / 10 * farm_amount
            basic.pause(13000)
            Farm_power += Farm_power / 10 * farm_amount / -1
        } else if (gold_action == 4) {
            mine_power += mine_power / 10 * mine_amount
            basic.pause(13000)
            mine_power += mine_power / 10 * mine_amount * -1
        } else if (gold_action == 5) {
            factory_power += factory_power / 10 * factory_amount
            basic.pause(13000)
            factory_power += factory_power / 10 * factory_amount / -1
        } else {
            bank_power += bank_power / 10 * bank_amount
            basic.pause(13000)
            bank_power += bank_power / 10 * bank_amount * -1
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    if (mode == 0) {
        if (cookies == upgrade_price) {
            if (upgrade_loop == 0) {
                upgrade_loop += 1
                Upgrade_no_2 += 1
                upgrade_no = Upgrade_no_2
            } else {
                Upgrade_no_2 += 1
                upgrade_loop = 0
                upgrade_no = 2
            }
            click_power += 1
            upgrade_price += 100
            if (upgrade_no == 1) {
                click_power += click_power
            } else if (upgrade_no == 2) {
                cps_multi += cps_multi / 5
            } else if (upgrade_no == 3) {
                gma_power += gma_power
            } else if (upgrade_no == 5) {
                click_power += click_power
            } else if (upgrade_no == 7) {
                Farm_power += Farm_power
            } else if (upgrade_no == 9) {
                click_power += click_power
            } else if (upgrade_no == 11) {
                mine_power += mine_power
            } else if (upgrade_no == 13) {
                click_power += click_power
            } else if (upgrade_no == 15) {
                factory_power += factory_power
            }
            cookies += upgrade_price * -1
        } else {
            basic.showIcon(IconNames.Sad)
        }
    } else if (mode == 1) {
        if (cookies >= mine_price) {
            cookies += -1 * mine_price
            cps += mine_power
            mine_price += Math.round(mine_price / 2)
            mine_amount += 1
        } else {
            basic.showIcon(IconNames.Sad)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (mode == 0) {
        if (cookies >= gma_price) {
            cookies += -1 * gma_price
            cps += gma_power
            gma_price += Math.round(gma_price / 2)
            Gma_amount += 1
        } else {
            basic.showIcon(IconNames.Sad)
        }
    } else if (mode == 1) {
        if (cookies >= Farm_price) {
            cookies += -1 * Farm_price
            cps += Farm_power
            Farm_price += Math.round(Farm_price / 2)
            farm_amount += 1
        } else {
            basic.showIcon(IconNames.Sad)
        }
    }
})
input.onGesture(Gesture.Shake, function () {
    if (mode == 0) {
        mode += 1
        basic.showString("M2")
    } else {
        mode = 0
        basic.showString("M1")
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (mode == 0) {
        if (cookies >= bank_price) {
            cookies += -1 * bank_price
            cps += bank_power
            bank_price += Math.round(bank_price / 2)
            bank_amount += 1
        } else {
            basic.showIcon(IconNames.Sad)
        }
    } else if (mode == 1) {
        if (cookies >= factory_price) {
            cookies += -1 * factory_price
            cps += factory_power
            factory_price += Math.round(factory_price / 2)
            factory_amount += 1
        } else {
            basic.showIcon(IconNames.Sad)
        }
    }
})
let cps_total = 0
let cps = 0
let upgrade_loop = 0
let gold_action = 0
let bank_amount = 0
let factory_amount = 0
let mine_amount = 0
let farm_amount = 0
let Gma_amount = 0
let bank_power = 0
let bank_price = 0
let factory_power = 0
let factory_price = 0
let mine_power = 0
let mine_price = 0
let Farm_price = 0
let gma_power = 0
let upgrade_no = 0
let cookies = 0
let gma_price = 0
let click_power = 0
let upgrade_price = 0
let cps_multi = 0
let Upgrade_no_2 = 0
let Farm_power = 0
let mode = 0
let gold_cookie = false
let G_CPS_Multi = 0
let G_Click_Multi = 0
G_Click_Multi = 1
G_CPS_Multi = 1
let gold_miss = 0
gold_cookie = false
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
loops.everyInterval(randint(180000, 300000), function () {
    if (gold_miss == 0) {
        basic.pause(2000)
        gold_miss += 1
    } else {
        gold_cookie = true
        basic.pause(10000)
        gold_cookie = false
    }
})
basic.forever(function () {
    if (gold_cookie == true) {
        cps_total = cps * (cps_multi * G_CPS_Multi)
        cookies += cps_total
        basic.showString("!G!")
        basic.showNumber(cookies)
    } else {
        cps_total = cps * (cps_multi * G_CPS_Multi)
        cookies += cps_total
        basic.showNumber(cookies)
    }
})
