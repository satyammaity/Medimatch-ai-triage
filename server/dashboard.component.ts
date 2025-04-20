import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnInit {
  patients: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getPatients().subscribe({
      next: (res) => {
        this.patients = res;
      },
      error: (err) => {
        console.error(err);
        alert('Failed to fetch patient data.');
      }
    });
  }
}