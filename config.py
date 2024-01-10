#!/usr/bin/env python3

# TODO some can be generated by setup

srvname     = 'kdlp.underground.software'
production  = False
refresh     = 0

appname     = 'orbit'
version     = '0.1'
source      = 'https://github.com/underground-software/orbit'
docsrc      = 'https://github.com/underground-software/kdlp.underground.software'

radius_port = '9098'

smtp_port   = '1465'
smtp_port_ext= '465'

pop3_port   = '1995'
pop3_port_ext= '995'

matrix_port = '8448'

# make exernal GET request to find these documents
logo_get    = '/images/kdlp_logo.png'
style_get   = '/style.css'

# this is also hard-coded in many files
orbit_root   = '/orbit'

# read these documents from a filesystem path
dataroot    = f'{orbit_root}/docs'
# TODO: this will become /var/orbit/databse/orbit.db or something
database    = f'{orbit_root}/orbit.db'
basedata    = f'{orbit_root}/default.orbit.db.dump'

email_dir   = f'{orbit_root}/email'

# duration of authentication token validity period
ses_mins    = 180

title       = 'Kernel Development Learning Pipeline'
nav_buttons = [
    (       '/index.md', 'Home'     ),
    ('/course/index.md', 'Course'   ),
    (          '/login', 'Login'    ),
    (       '/register', 'Register' ),
    (      '/dashboard', 'Dashboard'),
    (         '/who.md', 'Who'      ),
    (        '/info.md', 'Info'     ),
    (           '/cgit', 'Git'      )]

sql_verbose = False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Pass config var name as argument", file=sys.stderr)
        sys.exit(1)
    else:
        print(locals()[sys.argv[1]])
