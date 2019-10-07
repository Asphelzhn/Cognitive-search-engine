import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { SearchHitsComponent } from './search-page/search-hits/search-hits.component';
import { ResultBarComponent } from './search-page/search-hits/result-bar/result-bar.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { UploadFileComponent } from './admin-page/upload-file/upload-file.component';
import { StartPageComponent } from './start-page/start-page.component';
import { UploadedFileComponent } from './admin-page/uploaded-file/uploaded-file.component';


@NgModule({
  declarations: [
    AppComponent,
    SearchPageComponent,
    SearchBarComponent,
    SearchHitsComponent,
    ResultBarComponent,
    AdminPageComponent,
    UploadFileComponent,
    StartPageComponent,
    UploadedFileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
