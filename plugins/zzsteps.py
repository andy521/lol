# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  steps.py importado.{/cyan}'))

hideBoard = types.ReplyKeyboardHide()

reply_to_msg = list()
send_msg = list()

languages = {
    "ESPAÑOL": "es",
    "ENGLISH": "en",
    "ITALIANO": "it",
    "POLSKI": "pl",
    "DEUTSCH": "de",
    "FRANÇAIS": "fr",
    "PERSIAN": "fa",
    "PORTUGUÊS": "pt",
    "РУССКИЙ": "ru",
    "ไทย": "th",
    "ΕΛΛΗΝΙΚΆ": "el"
}


@bot.message_handler(
    func=lambda msg: next_step_handler(msg.chat.id) == 'start')
def step_start(m):
    cid = m.chat.id
    if m.content_type == 'text':
        if m.text in languages:
            users[
                str(cid)] = {
                "lang": languages[
                    m.text],
                "banned": False,
                "notify": True,
                "server": "",
                "summoner": ""}
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['lang_error']['en'] %
                (m.text, m.text), parse_mode="Markdown")
            return None
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
        for id in admins:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(id, "Nuevo usuario\n\nNombre: " +
                             str(m.from_user.first_name) +
                             "\nAlias: @" +
                             str(m.from_user.username) +
                             "\nID: " +
                             str(cid) +
                             "\nIdioma: " +
                             str(lang(cid)))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid, responses['start_2'][
                lang(cid)], reply_markup=hideBoard)
        userStep[cid] = 0


@bot.message_handler(
    func=lambda msg: next_step_handler(msg.chat.id) == 'contact')
def step_contact(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        for x in admins:
            bot.send_chat_action(x, 'typing')
            try:
                bot.send_message(x, contact_format(m), parse_mode="Markdown")
            except:
                bot.send_message(x, contact_format(m))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['contact_2'][lang(cid)])


@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'lang')
def step_lang(m):
    cid = m.chat.id
    if m.content_type == 'text':
        if m.text in languages:
            users[str(cid)]['lang'] = languages[m.text]
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['lang_error'][
                    lang(cid)] %
                (m.text, m.text), parse_mode="Markdown")
            return None
        userStep[cid] = 0
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid, responses['lang_2'][
                lang(cid)], reply_markup=hideBoard)


@bot.message_handler(func=lambda msg: next_step_handler(
    msg.chat.id) == 'update_rotation_text')
def step_update_rotation_text(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        with open('extra_data/rotation.txt', 'w') as f:
            f.write(m.text)
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['update_rotation_text_2'])


@bot.message_handler(func=lambda msg: next_step_handler(
    msg.chat.id) == 'update_rotation_pic', content_types=['photo'])
def step_update_rotation_pic(m):
    cid = m.chat.id
    userStep[cid] = 0
    file_id = m.photo[-1].file_id
    extra['rotation'] = file_id
    with open('extra_data/extra.json', 'w') as f:
        json.dump(extra, f)
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, responses['update_rotation_pic_2'])


@bot.message_handler(func=lambda msg: next_step_handler(
    msg.chat.id) == 'update_sale_text')
def step_update_sale_text(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        with open('extra_data/sale.txt', 'w') as f:
            f.write(m.text)
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['update_sale_text_2'])


@bot.message_handler(func=lambda msg: next_step_handler(
    msg.chat.id) == 'update_sale_pic', content_types=['photo'])
def step_update_sale_pic(m):
    cid = m.chat.id
    userStep[cid] = 0
    file_id = m.photo[-1].file_id
    extra['sale'] = file_id
    with open('extra_data/extra.json', 'w') as f:
        json.dump(extra, f)
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, responses['update_sale_pic_2'])


@bot.message_handler(
    func=lambda msg: next_step_handler(
        msg.chat.id) in [
            'patch_es',
            'patch_en',
            'patch_it',
            'patch_pl',
            'patch_fr',
            'patch_de',
            'patch_pt',
            'patch_fa',
            'patch_th',
            'patch_ru',
            'patch_el'])
def step_update_patch(m):
    cid = m.chat.id
    if m.content_type == 'text':
        with open('extra_data/patch_' + userStep[cid].split('_')[1] + '.txt', 'w') as f:
            f.write(m.text)
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            "Actualizado *patch_" +
            userStep[cid].split('_')[1] +
            ".txt*",
            parse_mode="Markdown")
        userStep[cid] = 0


@bot.message_handler(
    func=lambda msg: next_step_handler(msg.chat.id) == 'region')
def step_region(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        if m.text.upper() in ['EUW', 'EUNE', 'BR', 'NA',
                              'LAS', 'LAN', 'KR', 'TR', 'RU', 'OCE']:
            users[str(cid)]['server'] = m.text.lower()
            bot.send_message(
                cid,
                responses['region_success'][
                    lang(cid)] %
                (m.text.upper()),
                parse_mode="Markdown",
                reply_markup=hideBoard)
        else:
            bot.send_message(
                cid, responses['region_failure'][
                    lang(cid)], reply_markup=hideBoard)
            return None
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)


@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'name')
def step_name(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        bot.send_message(cid, responses['name_2'][lang(cid)])
        users[str(cid)]['summoner'] = m.text
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
