import math

import pynewtonmath as newton
from certifi.__main__ import args
from telegram import Update
from telegram.ext import CallbackContext

from IHbot import dispatcher
from IHbot.modules.disable import DisableAbleCommandHandler


def join(args):
    x = ''.join(map(str, args))
    return x


def simplify(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.simplify('{}'.format(join(args))))


def factor(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.factor('{}'.format(join(args))))


def derive(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.derive('{}'.format(join(args))))


def integrate(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.integrate('{}'.format(join(args))))


def zeroes(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.zeroes('{}'.format(join(args))))


def tangent(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.tangent('{}'.format(join(args))))


def area(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(newton.area('{}'.format(join(args))))


def cos(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))


def sin(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))


def tan(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))


def arccos(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))


def arcsin(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))


def arctan(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))


def abs(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))


def log(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))


__help__ = """
Solves complex math problems using https://newton.now.sh
 - /simplify: Simplify `/simplify 2^2+2(2)`
 - /factor: Factor `/factor x^2 + 2x`
 - /derive: Derive `/derive x^2+2x`
 - /integrate: Integrate `/integrate x^2+2x`
 - /zeroes: Find 0's `/zeroes x^2+2x`
 - /tangent: Find Tangent `/tangent 2lx^3`
 - /area: Area Under Curve `/area 2:4lx^3`
 - /cos: Cosine `/cos pi`
 - /sin: Sine `/sin 0`
 - /tan: Tangent `/tan 0`
 - /arccos: Inverse Cosine `/arccos 1`
 - /arcsin: Inverse Sine `/arcsin 0`
 - /arctan: Inverse Tangent `/arctan 0`
 - /abs: Absolute Value `/abs -1`
 - /log: Logarithm `/log 2l8`
__Keep in mind__: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
"""

__mod_name__ = "Math"

SIMPLIFY_HANDLER = DisableAbleCommandHandler("simplify", simplify, pass_args=True, run_async=True)
FACTOR_HANDLER = DisableAbleCommandHandler("factor", factor, pass_args=True, run_async=True)
DERIVE_HANDLER = DisableAbleCommandHandler("derive", derive, pass_args=True, run_async=True)
INTEGRATE_HANDLER = DisableAbleCommandHandler("integrate", integrate, pass_args=True, run_async=True)
ZEROES_HANDLER = DisableAbleCommandHandler("zeroes", zeroes, pass_args=True, run_async=True)
TANGENT_HANDLER = DisableAbleCommandHandler("tangent", tangent, pass_args=True, run_async=True)
AREA_HANDLER = DisableAbleCommandHandler("area", area, pass_args=True, run_async=True)
COS_HANDLER = DisableAbleCommandHandler("cos", cos, pass_args=True, run_async=True)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin, pass_args=True, run_async=True)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan, pass_args=True, run_async=True)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos, pass_args=True, run_async=True)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin, pass_args=True, run_async=True)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan, pass_args=True, run_async=True)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs, pass_args=True, run_async=True)
LOG_HANDLER = DisableAbleCommandHandler("log", log, pass_args=True, run_async=True)

dispatcher.add_handler(SIMPLIFY_HANDLER)
dispatcher.add_handler(FACTOR_HANDLER)
dispatcher.add_handler(DERIVE_HANDLER)
dispatcher.add_handler(INTEGRATE_HANDLER)
dispatcher.add_handler(ZEROES_HANDLER)
dispatcher.add_handler(TANGENT_HANDLER)
dispatcher.add_handler(AREA_HANDLER)
dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)
