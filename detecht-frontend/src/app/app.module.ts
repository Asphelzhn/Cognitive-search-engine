import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {PdfViewerModule} from 'ng2-pdf-viewer';
import {MatDialogModule} from '@angular/material';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations';
import {MAT_DIALOG_DEFAULT_OPTIONS} from '@angular/material/dialog';
import { FileSaverModule } from 'ngx-filesaver';
import {NgxKjuaModule} from 'ngx-kjua';
import { MatToolbarModule, MatIconModule, MatSidenavModule, MatListModule, MatButtonModule } from '@angular/material';
import {MatTabsModule} from '@angular/material';
import {ReactiveFormsModule} from '@angular/forms';

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
import {SearchResultPreviewComponent} from './search-page/search-result-preview/search-result-preview.component';
import { SearchHitPreviewComponent } from './search-page/search-hit-preview/search-hit-preview.component';
import { QrCodeComponent } from './search-page/search-hits/result-bar/qr-code/qr-code.component';
import { SavedDocumentsPageComponent } from './saved-documents-page/saved-documents-page.component';
import { LoginPageComponent } from './admin-page/login-page/login-page.component';
import { AdminNavbarComponent } from './admin-page/admin-navbar/admin-navbar.component';
import { RelatedSearchesDecisionTreeComponent } from './search-page/related-searches-decision-tree/related-searches-decision-tree.component';
import { EditDocumentsComponent } from './admin-page/edit-documents/edit-documents.component';
import { FooterComponent } from './footer/footer.component';
import { StatsComponent } from './admin-page/analytics/stats/stats.component';
import {DocumentStatsComponent} from './admin-page/analytics/document-stats/document-stats.component';
import { TrendingDocumentsComponent } from './start-page/trending-documents/trending-documents.component';
import { TrendingDocumentComponent } from './start-page/trending-documents/trending-document/trending-document.component';
import { SavedDocumentComponent } from './saved-documents-page/saved-document/saved-document.component';

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
    TrendingDocumentsComponent,
    TrendingDocumentComponent,
    SavedDocumentsPageComponent,
    LoginPageComponent,
    AdminNavbarComponent,
    RelatedSearchesDecisionTreeComponent,
    EditDocumentsComponent,
    FooterComponent,
    StatsComponent,
    DocumentStatsComponent,
    SavedDocumentComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    PdfViewerModule,
    MatDialogModule,
    NoopAnimationsModule,
    FileSaverModule,
    NgxKjuaModule,
    AppRoutingModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatButtonModule,
    MatIconModule,
    MatTabsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
  ],
  providers: [{provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}],
  bootstrap: [AppComponent],
  entryComponents: [SearchHitPreviewComponent]
})
export class AppModule { }
