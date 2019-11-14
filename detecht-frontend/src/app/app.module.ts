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
import { SentenceHitsComponent } from './search-page/search-hits/sentence-hits/sentence-hits.component';
import {MatDialogModule} from '@angular/material';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations';
import {MAT_DIALOG_DEFAULT_OPTIONS} from '@angular/material/dialog';
import { FileSaverModule } from 'ngx-filesaver';
import { QrCodeComponent } from './search-page/search-hits/result-bar/qr-code/qr-code.component';
import {NgxKjuaModule} from 'ngx-kjua';
import { TrendingDocumentsComponent } from './start-page/trending-documents/trending-documents.component';
import { TrendingDocumentComponent } from './start-page/trending-documents/trending-document/trending-document.component';

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
    SentenceHitsComponent,
    QrCodeComponent,
    TrendingDocumentsComponent,
    TrendingDocumentComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    PdfViewerModule,
    MatDialogModule,
    NoopAnimationsModule,
    FileSaverModule,
    NgxKjuaModule
  ],
  providers: [{provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}],
  bootstrap: [AppComponent],
  entryComponents: [SentenceHitsComponent]
})
export class AppModule { }
