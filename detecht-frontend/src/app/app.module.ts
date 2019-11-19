import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
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
import { AnalyticsComponent } from './admin-page/analytics/analytics.component';
import { RelatedSearchHitsComponent } from './search-page/related-search-hits/related-search-hits.component';
import { RelatedResultBarComponent } from './search-page/related-search-hits/related-result-bar/related-result-bar.component';
import { SearchResultPreviewComponent} from './search-page/search-result-preview/search-result-preview.component';
import { PdfViewerModule} from 'ng2-pdf-viewer';
import { SearchHitPreviewComponent } from './search-page/search-hit-preview/search-hit-preview.component';
import { MatDialogModule } from '@angular/material';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MAT_DIALOG_DEFAULT_OPTIONS } from '@angular/material/dialog';
import { FileSaverModule } from 'ngx-filesaver';
import { QrCodeComponent } from './search-page/search-hits/result-bar/qr-code/qr-code.component';
import { NgxKjuaModule } from 'ngx-kjua';
import { SavedDocumentsPageComponent } from './saved-documents-page/saved-documents-page.component';
import { LoginPageComponent } from './admin-page/login-page/login-page.component';
import { AdminNavbarComponent } from './admin-page/admin-navbar/admin-navbar.component';
import { RelatedSearchesDecisionTreeComponent } from './search-page/related-searches-decision-tree/related-searches-decision-tree.component';
import { EditDocumentsComponent } from './admin-page/edit-documents/edit-documents.component';
import { FooterComponent } from './footer/footer.component';
import {MatIconModule} from "@angular/material/icon";
import {FileUploadModule} from "ng2-file-upload";
import {MatCardModule} from "@angular/material/card";

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
    AnalyticsComponent,
    RelatedSearchHitsComponent,
    RelatedResultBarComponent,
    SearchResultPreviewComponent,
    SearchHitPreviewComponent,
    QrCodeComponent,
    SavedDocumentsPageComponent,
    LoginPageComponent,
    AdminNavbarComponent,
    RelatedSearchesDecisionTreeComponent,
    EditDocumentsComponent,
    FooterComponent,
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
    NgxKjuaModule,
    MatIconModule,
    FileUploadModule,
    MatCardModule,
    ReactiveFormsModule
  ],
  providers: [{provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}],
  bootstrap: [AppComponent],
  entryComponents: [SearchHitPreviewComponent]
})
export class AppModule { }
