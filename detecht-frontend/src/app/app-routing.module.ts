import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { UploadFileComponent } from './admin-page/upload-file/upload-file.component';
import { StartPageComponent } from './start-page/start-page.component';
import {SavedDocumentsPageComponent} from './saved-documents-page/saved-documents-page.component';
import {LoginPageComponent} from './admin-page/login-page/login-page.component';
import {EditDocumentsComponent} from "./admin-page/edit-documents/edit-documents.component";


const routes: Routes = [
  {path: '', component: StartPageComponent },
  { path: 'search', component: SearchPageComponent },
  { path: 'saved', component: SavedDocumentsPageComponent },
  { path: 'login', component: LoginPageComponent },
  { path: 'admin', component: AdminPageComponent },
  { path: 'upload', component: UploadFileComponent },
  { path: 'edit', component: EditDocumentsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
