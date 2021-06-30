import i18n

# Change the directory to the folder which contains the translation files
i18n.load_path.append('/Users/aniamritapc/PycharmProjects/pythonProject8/translations')

def load_lang_pref(lang_pref,word):
    i18n.set('locale', 'sg')
    if lang_pref == 1:
        i18n.set('fallback', 'en')
    elif lang_pref == 2:
        i18n.set('fallback', 'zh')
    elif lang_pref == 3:
        i18n.set('fallback', 'ml')
    else:
        i18n.set('fallback', 'en')
    print(i18n.t('translate.'+word))


load_lang_pref(1, "how are you")
load_lang_pref(2,"how are you")
load_lang_pref(2,"hi")
load_lang_pref(3,"how are you")
