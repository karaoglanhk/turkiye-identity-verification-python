from setuptools import setup

setup(
    name='turkiye_identity_verification',
    version='1.0.0',
    description='Using the Nüfus ve Vatandaşlık İşleri (NVİ), it verifies the information on the Turkish Identity Card.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hüseyin Karaoğlan',
    author_email='hkkaraoglan@icloud.com',
    license='MIT',
    keywords=['nvi', 'turkiye', 'identity', 'verification', 'verify', 'turkey', 'nufus', 'kimlik', 'dogrulama', 'yabanci', 'tckn', 'ykn'],
    packages=['turkiye_identity_verification']
)