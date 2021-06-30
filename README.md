# i18nPython
Its a 3 step process : 

  
1. Add both python-18n and pyYAML to the requirements 

python-i18n==0.3.9

PyYAML==5.4.1

2. Add translations in the translations folder as translate.<2letter>.yml file 
  For eg. translate.en.yml will contain 
  en:
  hi: Hello world !
  how are you : How are you ?
  
3. Load the i18n folder 

i18n.load_path.append('/Users/aniamritapc/PycharmProjects/pythonProject8/translations')

i18n.set('locale', 'sg')

i18n.set('fallback', 'en') # set language preferences based on usecase 

print(i18n.t('translate.hi)) # invoke i18n.t to translate
