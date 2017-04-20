# asterisk-sounds-core
NethServer RPM for asterisk-sounds-core
Based on Sangoma source RPM

## How to build

make-srpm asterisk-sounds-core.spec
srpm=$(basename "$(grep '^Wrote: ' build.log | tail -1 )")
mock -D "dist .ns7" --resultdir=. -r nethserver-7-x86_64 $srpm
