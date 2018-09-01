user='weblogic'
password='weblogic'
url='t3://localhost:7001'
connect(user, password, url)
edit()
cd('Servers/<ServerName>')
startEdit()
set('DebugHttp','true')
set('DebugHttpLogging','true')
set('DebugHttpSessions','true')


r--   CustomIdentityKeyStoreFileName               null
r--   CustomIdentityKeyStorePassPhrase             ******
r--   CustomIdentityKeyStorePassPhraseEncrypted    ******
r--   CustomIdentityKeyStoreType                   null
r--   CustomTrustKeyStoreFileName                  null
r--   CustomTrustKeyStorePassPhrase                ******
r--   CustomTrustKeyStorePassPhraseEncrypted       ******
r--   CustomTrustKeyStoreType                      null
save()
activate()
