/*
 * Copyright (C) 2006-2025 The LightCAS project
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; If not, see <https://www.gnu.org/licenses/>
 */

#pragma once

#include "debug.h"
#include "function.h"
#include "lcvector.h"

typedef CVector<class CElement *> CElementArray;

class CElement
{

private:
  typedef enum
  {
    ELEM_CONST,
    ELEM_VAR,
    ELEM_FUNCT,
    ELEM_NUM,
  } ELEM_TYPE;

  CString m_Name;
  CString m_Message;
  CFunction m_Function;
  ELEM_TYPE m_Type;
  bool m_Global;
  bool m_bAux;
  OP_CODE m_Ref;
  unsigned m_Index;

public:
  void Display(CDisplay &ds) const;
  void RemoveRules();
  void SetEquation(const CMathExpression &equ);
  void AddFunction(const CMathExpression &src, const CMathExpression &dst, unsigned line_nb = 0);

  const CString &GetName() const { return m_Name; }
  void SetName(const CString &name) { m_Name = name; }
  void SetFunct() { m_Type = ELEM_FUNCT; }
  void SetVar() { m_Type = ELEM_VAR; }
  void SetConst() { m_Type = ELEM_CONST; }
  void SetNumeric() { m_Type = ELEM_NUM; }
  void SetIndex(unsigned index)
  {
    m_Index = index;
    m_Ref = (OP_CODE)index;
  }
  void SetOperandNb(unsigned operand_nb)
  {
    SetFunct();
    ASSERT(CElementDataBase::GetOperandNb(m_Ref) == 0);
    ASSERT(operand_nb <= 3);
    m_Ref = CElementDataBase::Pack(m_Index, operand_nb);
#if (DEBUG_LEVEL > 0)
    CDisplay ds;
    ds += "SetParamNb   : ";
    Display(ds);
    ds += ':';
    ds += CString(operand_nb);
    ds.Log(LOG_DEBUG);
#endif
  }
  void SetGlobal(bool global) { m_Global = global; }
  void SetAux(bool bAux = true) { m_bAux = bAux; }
  void SetRef(OP_CODE op) { m_Ref = op; }
  void SetMessage(const CString &message) { m_Message = message; }
  unsigned GetOperandNb() const { return CElementDataBase::GetOperandNb(m_Ref); }
  bool IsVar() const { return (m_Type == ELEM_VAR); }
  bool IsConst() const { return (m_Type == ELEM_CONST); }
  bool IsFunct() const { return (m_Type == ELEM_FUNCT); }
  bool IsNumeric() const { return (m_Type == ELEM_NUM); }
  bool IsAux() const { return m_bAux; }
  bool IsGlobal() const { return m_Global; }
  bool IsVoid() const { return (GetOperandNb() == 0); }
  bool IsUnary() const { return (GetOperandNb() == 1); }
  bool IsBinary() const { return (GetOperandNb() == 2); }
  bool HasMessage() const { return (!m_Message.IsEmpty()); }
  OP_CODE ToRef() const { return m_Ref; }
  const CFunction *GetFunction() const { return &m_Function; }
  CFunction *GetFunction() { return &m_Function; }
  const CString &GetMessage() const { return m_Message; }

  explicit CElement(const CString &name);
  virtual ~CElement();
};
