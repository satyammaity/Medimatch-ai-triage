import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  patientName = '';
  textInput = '';
  selectedFile: File | null = null;
  response: any = null;
  isLoading = false;
  isDarkMode = false;

  constructor(private apiService: ApiService) {}

  toggleDarkMode() {
    this.isDarkMode = !this.isDarkMode;
    document.body.classList.toggle('dark-mode', this.isDarkMode);
  }

  useMic() {
    const recognition = new (window as any).webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.onresult = (e: any) => {
      this.textInput = e.results[0][0].transcript;
    };
    recognition.onerror = () => alert('Mic not working.');
    recognition.start();
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
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
      alert('Provide audio or text');
      return;
    }

    this.isLoading = true;
    this.apiService.transcribe(formData).subscribe({
      next: (res: any) => {
        this.response = res;
        window.open(`http://localhost:5000${res.pdf_url}`, '_blank');
        this.isLoading = false;
      },
      error: () => {
        alert('Error uploading.');
        this.isLoading = false;
      }
    });
  }
}
