import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {
  patientName: string = '';
  textInput: string = '';
  selectedFile: File | null = null;
  response: any = null;
  isDark: boolean = false;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    // Set default to light mode on load
    document.body.classList.add('light-mode');
  }

  toggleTheme() {
    this.isDark = !this.isDark;

    const body = document.body;
    if (this.isDark) {
      body.classList.remove('light-mode');
      body.classList.add('dark-mode');
    } else {
      body.classList.remove('dark-mode');
      body.classList.add('light-mode');
    }
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0] || null;
  }

  onSubmit(event: Event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', this.patientName);

    if (this.selectedFile) {
      formData.append('audio', this.selectedFile);
    } else if (this.textInput.trim()) {
      formData.append('text', this.textInput.trim());
    } else {
      alert('Please upload an audio file or enter symptom text.');
      return;
    }

    this.apiService.transcribe(formData).subscribe({
      next: (res) => {
        this.response = res;

        // Full download URL using backend port
        const fileUrl = http://localhost:5000${res.pdf_url};
        window.open(fileUrl, '_blank');
      },
      error: (err) => {
        console.error(err);
        alert('Something went wrong while submitting.');
      }
    });
  }
}