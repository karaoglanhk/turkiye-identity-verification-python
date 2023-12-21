# Example

```python
from turkiye_identity_verification import native_citizen_verify, foreign_citizen_verify


# If want native citizen verify
verifyIdentityForNativeCitizen = native_citizen_verify(11111111111,'Hüseyin', 'Karaoğlan',2000)

print(verifyIdentityForNativeCitizen) # True or False



# If want foreign citizen verify
verifyIdentityForForeignCitizen = foreign_citizen_verify(99111111111, 'Hüseyin', 'Karaoğlan', 1, 1, 2000)

print(verifyIdentityForForeignCitizen) # True or False
```