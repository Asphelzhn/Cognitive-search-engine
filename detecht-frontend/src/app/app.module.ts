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
import { RelatedSearchHitsComponent } from './search-page/related-search-hits/related-search-hits.component';
import { RelatedResultBarComponent } from './search-page/related-search-hits/related-result-bar/related-result-bar.component';
import {SearchResultPreviewComponent} from './search-page/search-result-preview/search-result-preview.component';
import {PdfViewerModule} from 'ng2-pdf-viewer';
import { StatsComponent } from './admin-page/stats/stats.component';
import {DocumentStatsComponent} from './admin-page/document-stats/document-stats.component';
import { SidebarComponent } from './admin-page/sidebar/sidebar.component';
import { MatToolbarModule, MatIconModule, MatSidenavModule, MatListModule, MatButtonModule } from '@angular/material';
import {MatTabsModule} from '@angular/material';
import {ReactiveFormsModule} from '@angular/forms';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';



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
    UploadedFileComponent,
    RelatedSearchHitsComponent,
    RelatedResultBarComponent,
    SearchResultPreviewComponent,
    StatsComponent,
    DocumentStatsComponent,
    SidebarComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    PdfViewerModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatButtonModule,
    MatIconModule,
    MatTabsModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
