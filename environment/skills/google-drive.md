# Skill: google-drive

## Description
Access files stored in Dana Serrano's Google Drive account.

## Base URL
`$GOOGLE_DRIVE_API_URL` (e.g., http://localhost:8080/drive)

## Endpoints

### GET /drive/files
List all files in Dana's Drive.

```bash
curl "$GOOGLE_DRIVE_API_URL/files"
```

### GET /drive/files/{file_id}
Get metadata for a specific file.

```bash
curl "$GOOGLE_DRIVE_API_URL/files/gdrive_cr_001"
```

## Notes
- Drive contains research documents, rotation schedules, and loan tracking files.
- Wedding expense files are stored locally in the workspace, not on Drive.
