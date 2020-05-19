import sys
import os
import argparse
import webbrowser

### Determine ambiente variables for Flask runner
os.environ['FLASK_ENV'] = "development"
os.environ['FLASK_APP'] = "bazar.run:create_app"

###
def main(args):
    """
    in construction 
    """
    
    # Processa os comandos inseridos


    args = parseCommandLine(args)

    ###
    if (args.dbmigrate is not None):
        print('Running command line' + args)
    
    elif (args.dbseed is not None):
        print('Running command line' + args)
    
    elif (args.makemigration is not None):
        print('Running command line' + args)
    
    elif (args.makeseeder is not None):
        print('Running command line' + args)
    
    else:
        print('###############################################')
        print('Open project on browser. Please press "F5" Key after server load!')
        
        webbrowser.open('http://localhost:' + args.server)

        print('###############################################')
        print('Running server in port: ' + args.server)
        print('###############################################')
        
        #####
        os.system('flask run --port ' + args.server)

    return 0


def parseCommandLine(args):
    """
    Parse commands for trader tool
    """
    
    description = "Use -h to list all commands."

    ####
    parser = argparse.ArgumentParser(description=description)

    ### Run server
    parser.add_argument('-s', '--server', nargs = '?', type = str, help = 'Run application in development', const = '5000')

    ### Database
    parser.add_argument('-migrate', '--dbmigrate', nargs = '?', type=str, help = 'Run all Migration', const = 'all')
    parser.add_argument('-seed', '--dbseed', nargs = '?', type=str, help = 'Run all database seeds', const = 'all')
    
    ### Make Commands
    parser.add_argument('-migration', '--makemigration', nargs = '+', type = str, help = 'Create a new migration file')
    parser.add_argument('-seeder', '--makeseeder', nargs = '+', type = str, help = 'Create a new seeder class')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
