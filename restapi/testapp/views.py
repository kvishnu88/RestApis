from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.views.generic import View
from testapp.mixins import SerializeMixin, HttpResponseMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self,request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not available '})
            return self.render_to_http_response(json_data, status=404)
            # return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            json_data = self.serialize([emp,])
        return self.render_to_http_response(json_data)

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'Record Not Found not able to update '})
            return self.render_to_http_response(json_data, status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_dada = json.dumps({'msg':'Please send valid json data only  '})
            return self.render_to_http_response(json_dada, status=400)
        provided_dada = json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(provided_dada)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_dada = json.dumps({'msg': 'Resource updated successfully'})
            return self.render_to_http_response(json_dada)
        if form.errors:
            json_dada = json.dumps(form.errors)
            return self.render_to_http_response(json_dada, status=400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'Record Not Found not able to delete '})
            return self.render_to_http_response(json_data, status=404)
        status, deleted_item = emp.delete()
        print(deleted_item)
        if status == 1:
            json_dada = json.dumps({'msg': 'Resource deleted successfully'})
            return self.render_to_http_response(json_dada)
        json_dada = json.dumps({'msg': 'Unable to delete...plz try again '})
        return self.render_to_http_response(json_dada)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin, View):
    def get(self,request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_dada = json.dumps({'msg':'Please send valid json data only  '})
            return self.render_to_http_response(json_dada, status=400)
        emp_dada = json.loads(data)
        form = EmployeeForm(emp_dada)
        if form.is_valid():
            form.save(commit=True)
            json_dada = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_dada)
        if form.errors:
            json_dada = json.dumps(form.errors)
            return self.render_to_http_response(json_dada,status=400)