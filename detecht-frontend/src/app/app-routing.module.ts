import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminPageComponent } from './admin-page/admin-page.component';
import {SearchPageComponent} from './search-page/search-page.component';
import {UploadFileComponent} from './admin-page/upload-file/upload-file.component';


const routes: Routes = [
  { path: '', component: SearchPageComponent },
  { path: 'admin', component: AdminPageComponent },
  { path: 'upload', component: UploadFileComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
