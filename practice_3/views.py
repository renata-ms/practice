# Create your views here.
from django.shortcuts import render
import  os, time
# var 1
def listing(request, sub):
        context = { }
        if sub == '':
                context['dir_name'] = '/var/log'
                context['dir_content'] = os.listdir('/var/log')
        else:
                context['dir_name'] = '/var/log' + '/' + str(sub)
                context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
        return render(request, 'listing.html', context)
# var 2
def listing(request, sub):
        context = { }
        dir_name = '/var/log' + '/' + str(sub)
        context['dir_name'] = dir_name
        context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
        context['dir'] = []
        context['f'] = []
        for f in context['dir_content']:
                fullname = os.path.join(dir_name, f)
                if os.path.isdir(fullname):
                        context['dir'].append(f)
                else:
                        context['f'].append(f)
        return render(request, 'listing.html', context)
# var 3
def listing(request, sub):
        context = { }
        dir_name = '/var/log' + '/' + str(sub)
        context['dir_name'] = dir_name
        context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
        context['tbl_content'] = []
        for f in context['dir_content']:
                row = []
                fullname = os.path.join(dir_name, f)
                size = os.path.getsize(fullname)
                stat = os.stat(fullname)
                time = time.localtime(stat.st_mtime)
                cat = str(t[2])+'/'+str(t[1])+'/'+str(t[0])+' '+str(t[3])+':'+str(t[4])+':'+str(t[5])
                row.append(f)
                row.append(size)
                row.append(cat)
                context['tbl_content'].append(row)
        return render(request, 'listing.html', context)

