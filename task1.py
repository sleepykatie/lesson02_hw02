import re


def email_parse(email):
    result_dict = {}
    # EMAIL_RE = re.compile(r'\w*@\w*\.\w*')
    EMAIL_RE = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+$')
    EMAIL_USERNAME_RE = re.compile(r'^.*?(?=@)')
    # EMAIL_USERNAME_RE = re.compile(r'^(\w*[.])\w*[^@]')
    EMAIL_DOMAIN_RE = re.compile(r'[^@]\w*\.\w*$')

    if not EMAIL_RE.match(email):
        print(f'wrong e-mail {email}')
        raise ValueError
    else:
        name_part = EMAIL_USERNAME_RE.findall(email)
        domain_part = EMAIL_DOMAIN_RE.findall(email)
        result_dict[name_part[0]] = domain_part[0]

    return result_dict


if __name__ == '__main__':

    e_mails = ['anna_k@mail.ru',
               'alena3478@gmail.com',
               'alisa@yandex.ru',
               'alina.alina@gmail.com',
               'alla_ivanova@gmailcom',
               'arina-567@mail.ru']
    for e_mail in e_mails:
        print(email_parse(e_mail))
