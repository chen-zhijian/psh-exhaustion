param(
    [switch]$Publish,
    [ValidateSet('pdflatex', 'xelatex')]
    [string]$Engine = 'xelatex',
    [string]$Executable,
    [string]$PdfLatex,
    [string]$IntakeSource,
    [string]$Python = 'python'
)

$ErrorActionPreference = 'Stop'
$buildArguments = @((Join-Path $PSScriptRoot 'build.py'), '--engine', $Engine)
if ($Publish) { $buildArguments += '--publish' }
if ($Executable) { $buildArguments += @('--executable', $Executable) }
if ($PdfLatex) { $buildArguments += @('--pdflatex', $PdfLatex) }
if ($IntakeSource) { $buildArguments += @('--intake-source', $IntakeSource) }
& $Python @buildArguments
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
