from django.shortcuts import render
# from django.db.models import Q
# Create your views here.
# class DataIndexView():
#     model = models.AccessionsData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import PhenotypeData
from .models import BaseModel
from .models import CabbageInfo
from .models import AccessionsData
import math


def index(request):
    return render(request, 'phenotype/index.html', {})
def info(request):
    return render(request, 'phenotype/info.html', {})

class table:
    def __init__(self,name,qs):
        

        LENGTH = 20
        NUM_COL = math.ceil(len(qs)/LENGTH)
        temp = []
        result = []
        for i in range(NUM_COL):
            temp.append(['']*LENGTH)

        for i in range(NUM_COL):
            for j in range(LENGTH):
                if i*LENGTH+j>=len(qs):
                    break
                temp[i][j] = qs[i*LENGTH+j]

        if len(temp) == 0:
            self.qs = [[]]
        else:
            for i in range(len(temp[0])):
                temp_column = []
                for j in range(len(temp)):
                    temp_column.append(temp[j][i])
                result.append(temp_column)

            self.qs = result

        self.name = "<tr><td style='padding:5px 15px 5px 10px;;' colspan='"+str(NUM_COL)+"'><h5>"+name+"</h5></td></tr>"


def post_list(request):

    qs = CabbageInfo.objects.all() #query set: 전체 포스팅 목록을 가져올 준비

    method_classfication = ["Non-pekinensis","Early accessions", "Contemporary accessions", "Chinese"]
    result_qs = []
    for c in method_classfication:
        temp = table(c,qs.filter(method_classfication=c))
        result_qs.append(temp)

    return render(request, 'phenotype/post_list.html', {
        'post_list': result_qs
    })



class PostDetailView(DetailView):
    context_object_name = 'object_list'
    model = CabbageInfo
    
    template_name = 'phenotype/post_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.object.pk
        context = super(PostDetailView, self).get_context_data(**kwargs)
        cabbage_qs = CabbageInfo.objects.filter(id=pk).all
        phenotype_qs = PhenotypeData.objects.filter(cabbage_id=pk).all
        # 검증 
         
        context["phenotypedata"] = phenotype_qs
        context["cabbageinfo"] = cabbage_qs
        return context
    




def genotype(request):

    qs = CabbageInfo.objects.all() #query set: 전체 포스팅 목록을 가져올 준비

    method_classfication = ["Non-pekinensis","Early accessions", "Contemporary accessions", "Chinese"]
    result_qs = []
    for c in method_classfication:
        temp = table(c,qs.filter(method_classfication=c))
        result_qs.append(temp)

    return render(request, 'genotype/genotype.html', {
        'genotype': result_qs
    })

 

class GenotyprDetailView(DetailView):
    context_object_name = 'object_list'
    model = CabbageInfo
    
    template_name = 'genotype/genotypeDetail.html'
    paginate_by = 10  # Display 10 objects per page
    
    def get_context_data( self, **kwargs):
        
        ROWS_PER_PAGE = 20
        pk = self.object.pk

        chrom = str(self.request.GET.get('chrom','A01'))
        context = super(GenotyprDetailView, self).get_context_data(**kwargs)
        cabbage_qs = CabbageInfo.objects.filter(id=pk).all
        phenotype_qs = PhenotypeData.objects.filter(cabbage_id=pk).all

        page = int(self.request.GET.get('p',1))
        # accessions_qs = AccessionsData.objects.filter(cabbage_id=pk,format="GT",chrom=chrom)
        accessions_qs = AccessionsData.objects.raw("SELECT * FROM kribb.accessions_data where cabbage_id="+str(pk)+" and format='GT' and chrom='"+chrom+"' limit "+str(ROWS_PER_PAGE*5)+" offset "+str((page-1)*ROWS_PER_PAGE)+";")
        paginator = Paginator(accessions_qs, ROWS_PER_PAGE)

        context["phenotypedata"] = phenotype_qs
        context["cabbageinfo"] = cabbage_qs

        start = 0
        if len(accessions_qs)<ROWS_PER_PAGE*3:
            diff = 6-len(accessions_qs)//ROWS_PER_PAGE
            print(diff)
            start = page-diff
        else:
            start = page-3
            if page<4:
                start = 1

        end = start+7
        context["page_range"] = list(range(start,end))
        context["cur_page"] = page

        accessions_page = paginator.get_page(1)

        context["accessionsdata"] = accessions_page

        return context
       
        
    
    # def accessions_list(request):
    #     accessions_all = AccessionsData.objects.all().order_by('-id')
    #     page = int(request.GET.get('p', 1)) #없으면 1로 지정
    #     paginator = Paginator(accessions_all, 5) #한 페이지 당 몇개 씩 보여줄 지 지정 
    #     accessions = paginator.get_page(page)
    #     return render(request, "genotype/genotypeDetail.html", {"accessions":accessions})
