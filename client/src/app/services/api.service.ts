import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = '/api';  // 🔥 Proxy handles this

  constructor(private http: HttpClient) {}

  transcribe(data: FormData): Observable<any> {
    return this.http.post(`${this.baseUrl}/transcribe`, data);
  }
}
