import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { SearchHitsComponent } from './search-page/search-hits/search-hits.component';
import { ResultBarComponent } from './search-page/search-hits/result-bar/result-bar.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { UploadFileComponent } from './admin-page/upload-file/upload-file.component';
import { StartPageComponent } from './start-page/start-page.component';
import { RelatedSearchHitsComponent } from './search-page/related-search-hits/related-search-hits.component';
import { RelatedResultBarComponent } from './search-page/related-search-hits/related-result-bar/related-result-bar.component';

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
    RelatedSearchHitsComponent,
    RelatedResultBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
